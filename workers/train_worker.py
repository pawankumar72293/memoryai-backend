from workers.celery_worker import celery

from database.session import SessionLocal

from services.persona_service import (
    PersonaService
)


@celery.task
def train_persona_task(
    persona_id
):

    db = SessionLocal()

    try:

        PersonaService().train(
            db,
            persona_id
        )

    finally:

        db.close()