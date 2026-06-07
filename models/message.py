import uuid

from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy import Text
from sqlalchemy import ForeignKey
from sqlalchemy import DateTime

from sqlalchemy.sql import func

from database.base import Base


class Message(Base):

    __tablename__ = "messages"

    id = Column(
        String(36),
        primary_key=True,
        default=lambda: str(uuid.uuid4())
    )

    persona_id = Column(
        String(36),
        ForeignKey("personas.id")
    )

    sender = Column(
        String(255)
    )

    content = Column(
        Text
    )

    message_date = Column(
        String(100),
        nullable=True
    )
    
    created_at = Column(
        DateTime,
        server_default=func.now()
    )