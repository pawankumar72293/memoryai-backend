from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from schemas.persona import CreatePersonaSchema

from services.persona_service import PersonaService
from services.rag_service import (
    RagService
)

from services.persona_service import (
    PersonaService
)

from dependencies.auth import (
    get_db,
    get_current_user
)

from workers.train_worker import (
    train_persona_task
)

router = APIRouter()

@router.post("")
def create_persona(

    payload: CreatePersonaSchema,

    db: Session = Depends(get_db),

    current_user=Depends(
        get_current_user
    )

):

    service = PersonaService()

    return service.create(
        db,
        current_user,
        payload
    )

@router.get("")
def get_personas(
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    service = PersonaService()
    return service.get_all(db, current_user)

@router.get("/{persona_id}")
def get_persona(
    persona_id: str,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    service = PersonaService()
    persona = service.get_by_id(db, persona_id, current_user)
    if not persona:
        from fastapi import HTTPException
        raise HTTPException(status_code=404, detail="Persona not found")
    return persona

@router.post("/{persona_id}/train")
def train_persona(
    persona_id: str,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):

    train_persona_task.delay(
        persona_id
    )

    return {
        "message": "Training started"
    }