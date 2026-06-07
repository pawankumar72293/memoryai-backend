from models.conversation import Conversation

from services.embedding_service import (
    EmbeddingService
)

from services.qdrant_service import (
    QdrantService
)


class RagService:

    def retrieve_context(
        self,
        db,
        persona_id,
        user_message
    ):

        embedding = (
            EmbeddingService()
            .generate_embedding(
                user_message
            )
        )

        results = (
            QdrantService()
            .search(
                str(persona_id),
                embedding
            )
        )

        whatsapp_context = []

        for item in results:

            payload = item.payload

            whatsapp_context.append(
                f"{payload['sender']}: {payload['content']}"
            )

        recent_messages = (
            db.query(Conversation)
            .filter(
                Conversation.persona_id == persona_id
            )
            .order_by(
                Conversation.created_at.desc()
            )
            .limit(20)
            .all()
        )

        recent_context = []

        for chat in reversed(recent_messages):

            recent_context.append(
                f"User: {chat.user_message}"
            )

            recent_context.append(
                f"AI: {chat.ai_response}"
            )

        final_context = f"""
Recent Conversations:

{chr(10).join(recent_context)}

Past WhatsApp Messages:

{chr(10).join(whatsapp_context)}
"""

        return final_context