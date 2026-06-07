from fastapi import APIRouter
from fastapi import Depends
from core.logger import logger
from sqlalchemy.orm import Session

from dependencies.auth import get_db

from schemas.chat import ChatSchema

from services.ai_service import AIService
from services.rag_service import RagService
from models.conversation import Conversation
from repositories.conversation_repository import (
    ConversationRepository
)

from dependencies.auth import (
    get_current_user
)

router = APIRouter()


@router.post("/message")
def chat(
    payload: ChatSchema,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):

    logger.info(
        f"Chat request: {payload.message}"
    )
    
    context = (
        RagService()
        .retrieve_context(
            db,
            payload.persona_id,
            payload.message
        )
    )

    prompt = f"""
You are the uploaded persona.

You must behave exactly like them.

Context:

{context}

User:
{payload.message}

Rules:
- Never say you are an AI
- Reply naturally
- Match emotional tone
- Keep responses realistic
"""

    reply = (
        AIService()
        .generate(prompt)
    )

    ConversationRepository().create(
        db,
        {
            "user_id": current_user.id,
            "persona_id": payload.persona_id,
            "session_id": payload.session_id,
            "user_message": payload.message,
            "ai_response": reply
        }
    )

    return {
        "reply": reply
    }

@router.get("/history/{persona_id}")
def history(
    persona_id: str,
    session_id: str,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):

    rows = (
        db.query(Conversation)
        .filter(
            Conversation.persona_id == persona_id
        )
        .filter(
            Conversation.session_id == session_id
        )
        .order_by(
            Conversation.created_at.desc()
        )
        .limit(100)
        .all()
    )

    return rows