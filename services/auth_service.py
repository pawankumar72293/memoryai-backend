from repositories.user_repository import UserRepository
from core.security import (
    hash_password,
    verify_password,
    create_access_token
)
from fastapi import HTTPException
from fastapi import status

class AuthService:

    def register(
        self,
        db,
        payload
    ):

        repo = UserRepository()

        existing_user = repo.get_by_email(
            db,
            payload.email
        )

        if existing_user:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Email already exists"
            )

        data = payload.model_dump()

        data["password"] = hash_password(
            payload.password
        )

        return repo.create(
            db,
            data
        )

    def login(
        self,
        db,
        payload
    ):

        repo = UserRepository()

        user = repo.get_by_email(
            db,
            payload.email
        )

        if not user:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid email or password"
            )

        if not verify_password(
            payload.password,
            user.password
        ):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid email or password"
            )

        token = create_access_token(
            {
                "sub": str(user.id)
            }
        )

        return {
            "access_token": token,
            "token_type": "bearer"
        }