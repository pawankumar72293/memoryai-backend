import asyncio

from fastapi import APIRouter
from fastapi import WebSocket
from fastapi import WebSocketDisconnect

from database.session import SessionLocal

from services.rag_service import RagService
from services.ai_service import AIService

from repositories.conversation_repository import (
    ConversationRepository
)

from services.redis_service import (
    RedisService
)

router = APIRouter()


@router.websocket("/chat/{persona_id}")
async def websocket_chat(
    websocket: WebSocket,
    persona_id: str
):

    await websocket.accept()

    db = SessionLocal()

    RedisService().set(
        f"user:{persona_id}",
        "online"
    )

    try:

        while True:

            message = (
                await websocket.receive_text()
            )

            context = (
                RagService()
                .retrieve_context(
                    db,
                    persona_id,
                    message
                )
            )

            prompt = f"""
You are the uploaded persona.

You must behave exactly like them.

Context:

{context}

User:
{message}

Rules:
- Never say you are AI
- Reply naturally
- Match emotional tone
"""

            cache_key = f"{persona_id}:{message}"

            cached = (
                RedisService()
                .get(cache_key)
            )

            if cached:

                await websocket.send_text(
                    cached
                )

                continue

            await websocket.send_text(
                "__typing__"
            )

            reply = (
                AIService()
                .generate(prompt)
            )

            RedisService().set(
                cache_key,
                reply
            )

            ConversationRepository().create(
                db,
                {
                    "user_id": "ws-user",
                    "persona_id": persona_id,
                    "session_id": "ws-session",
                    "user_message": message,
                    "ai_response": reply
                }
            )

            partial = ""

            for word in reply.split():

                partial += word + " "

                await websocket.send_text(
                    partial
                )

                await asyncio.sleep(0.03)

    except WebSocketDisconnect:

        print(
            "Client disconnected"
        )

    finally:

        RedisService().delete(
            f"user:{persona_id}"
        )
        db.close()