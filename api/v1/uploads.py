from fastapi import APIRouter
from fastapi import UploadFile
from fastapi import File
from fastapi import Depends

from sqlalchemy.orm import Session

from dependencies.auth import (
    get_db,
    get_current_user
)

from services.upload_service import UploadService
from services.whatsapp_parser import WhatsAppParser

from repositories.upload_repository import UploadRepository
from repositories.message_repository import MessageRepository

from models.upload import Upload

router = APIRouter()


@router.post("/whatsapp")
async def upload_whatsapp_zip(

    persona_id: str,

    file: UploadFile = File(...),

    db: Session = Depends(get_db),

    current_user=Depends(
        get_current_user
    )

):

    upload_service = UploadService()

    file_path = upload_service.save_file(
        file
    )

    upload = Upload(
        user_id=current_user.id,
        persona_id=persona_id,
        file_name=file.filename,
        file_path=file_path,
        status="uploaded"
    )

    upload_repo = UploadRepository()

    upload_repo.create(
        db,
        upload
    )

    parser = WhatsAppParser()

    extract_dir = parser.extract_zip(
        file_path
    )

    chat_file = parser.find_chat_file(
        extract_dir
    )

    messages = parser.parse_chat(
        chat_file,
        persona_id
    )

    message_repo = MessageRepository()

    message_repo.bulk_create(
        db,
        messages
    )

    return {
        "messages_saved": len(messages),
        "chat_file": chat_file
    }