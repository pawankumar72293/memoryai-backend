from models.conversation import Conversation


class ConversationRepository:

    def create(
        self,
        db,
        data
    ):

        conversation = Conversation(
            **data
        )

        db.add(
            conversation
        )

        db.commit()

        db.refresh(
            conversation
        )

        return conversation