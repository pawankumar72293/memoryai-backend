import uuid

from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy import DateTime

from sqlalchemy.sql import func

from database.base import Base


class ChatSession(Base):

    __tablename__ = "chat_sessions"

    id = Column(
        String(36),
        primary_key=True,
        default=lambda: str(uuid.uuid4())
    )

    user_id = Column(
        String(36),
        nullable=False
    )

    persona_id = Column(
        String(36),
        nullable=False
    )

    title = Column(
        String(255)
    )

    created_at = Column(
        DateTime,
        server_default=func.now()
    )