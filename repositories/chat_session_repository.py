from models.chat_session import ChatSession


class ChatSessionRepository:

    def create(
        self,
        db,
        data
    ):

        session = ChatSession(
            **data
        )

        db.add(session)

        db.commit()

        db.refresh(session)

        return session