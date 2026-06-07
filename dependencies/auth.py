from fastapi import Depends

from fastapi.security import HTTPBearer
from fastapi.security import HTTPAuthorizationCredentials

from jose import jwt
from jose import JWTError

from sqlalchemy.orm import Session

from database.session import SessionLocal

from models.user import User

from core.security import (
    SECRET_KEY,
    ALGORITHM
)

from core.exceptions import (
    UnauthorizedException
)


def get_db():

    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()


security = HTTPBearer()


def get_current_user(

    credentials: HTTPAuthorizationCredentials = Depends(security),

    db: Session = Depends(get_db)

):

    token = credentials.credentials

    try:

        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )

        user_id = payload.get("sub")

    except JWTError:

        raise UnauthorizedException(
            "Invalid token"
        )

    user = (
        db.query(User)
        .filter(User.id == user_id)
        .first()
    )

    if not user:

        raise UnauthorizedException(
            "User not found"
        )

    return user