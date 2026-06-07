from models.message import Message


class MessageRepository:

    def bulk_create(
        self,
        db,
        messages
    ):

        db.add_all(messages)

        db.commit()

        return True