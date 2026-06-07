from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session
from pydantic import BaseModel
from typing import Optional

from dependencies.auth import (
    get_current_user
)
from dependencies.auth import get_db

router = APIRouter()

class UpdateProfileSchema(BaseModel):
    name: Optional[str] = None
    profile_image: Optional[str] = None

@router.get("/profile")
def profile(

    current_user = Depends(
        get_current_user
    )

):

    return {
        "id": current_user.id,
        "name": current_user.name,
        "email": current_user.email,
        "profile_image": current_user.profile_image
    }

@router.put("/profile")
def update_profile(
    payload: UpdateProfileSchema,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    if payload.name is not None:
        current_user.name = payload.name
    if payload.profile_image is not None:
        current_user.profile_image = payload.profile_image

    db.commit()
    db.refresh(current_user)

    return {
        "id": current_user.id,
        "name": current_user.name,
        "email": current_user.email,
        "profile_image": current_user.profile_image
    }