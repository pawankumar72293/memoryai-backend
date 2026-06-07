from models.persona import Persona
from models.message import Message

from repositories.persona_repository import (
    PersonaRepository
)

from services.embedding_service import (
    EmbeddingService
)

from services.qdrant_service import (
    QdrantService
)


class PersonaService:

    def create(
        self,
        db,
        current_user,
        payload
    ):

        repo = PersonaRepository()

        persona = Persona(
            user_id=current_user.id,
            name=payload.name,
            relationship=payload.relationship,
            description=payload.description
        )

        return repo.create(
            db,
            persona
        )

    def get_all(
        self,
        db,
        current_user
    ):
        repo = PersonaRepository()
        return repo.get_all(db, current_user.id)

    def get_by_id(
        self,
        db,
        persona_id,
        current_user
    ):
        repo = PersonaRepository()
        return repo.get_by_id(db, persona_id, current_user.id)


    def train(
        self,
        db,
        persona_id
    ):

        messages = (
            db.query(Message)
            .filter(
                Message.persona_id == persona_id
            )
            .all()
        )

        embeddings = []

        payloads = []

        for msg in messages:

            embedding = (
                EmbeddingService()
                .generate_embedding(
                    msg.content
                )
            )

            embeddings.append(
                embedding
            )

            payloads.append(
                {
                    "message_id": msg.id,
                    "content": msg.content,
                    "sender": msg.sender
                }
            )

        QdrantService().create_collection(
            str(persona_id)
        )

        QdrantService().insert_vectors(
            str(persona_id),
            embeddings,
            payloads
        )

        return {
            "status": "trained",
            "messages": len(messages)
        }