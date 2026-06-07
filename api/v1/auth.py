from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from schemas.auth import RegisterSchema
from schemas.auth import LoginSchema
from services.auth_service import AuthService

from dependencies.auth import get_db

router = APIRouter()


@router.post("/register")
def register(
    payload: RegisterSchema,
    db: Session = Depends(get_db)
):

    service = AuthService()

    return service.register(
        db,
        payload
    )

@router.post("/login")
def login(
    payload: LoginSchema,
    db: Session = Depends(get_db)
):

    service = AuthService()

    return service.login(
        db,
        payload
    )

@router.post("/logout")
def logout():
    return {"message": "Logged out successfully"}