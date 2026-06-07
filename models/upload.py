import uuid

from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy import ForeignKey
from sqlalchemy import DateTime

from sqlalchemy.sql import func

from database.base import Base


class Upload(Base):

    __tablename__ = "uploads"

    id = Column(
        String(36),
        primary_key=True,
        default=lambda: str(uuid.uuid4())
    )

    user_id = Column(
        String(36),
        ForeignKey("users.id")
    )

    persona_id = Column(
        String(36),
        ForeignKey("personas.id")
    )

    file_name = Column(String(255))

    file_path = Column(String(500))

    status = Column(
        String(50),
        default="uploaded"
    )

    created_at = Column(
        DateTime,
        server_default=func.now()
    )