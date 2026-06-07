from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from dependencies.auth import (
    get_db,
    get_current_user
)

from repositories.chat_session_repository import (
    ChatSessionRepository
)

router = APIRouter()


@router.post("/")
def create_session(
    persona_id: str,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):

    session = (
        ChatSessionRepository()
        .create(
            db,
            {
                "user_id": current_user.id,
                "persona_id": persona_id,
                "title": "New Chat"
            }
        )
    )

    return session