from fastapi import FastAPI
from fastapi.responses import JSONResponse

from fastapi.requests import Request

from fastapi import status
from middleware.logging import (
    LoggingMiddleware
)
from middleware.rate_limit import (
    RateLimitMiddleware
)
from api.v1.auth import router as auth_router
from api.v1.users import (
    router as user_router
)
from api.v1.personas import (
    router as persona_router
)

from api.v1.uploads import router as upload_router

from database.base import Base
from database.session import engine

from models.user import User
from models.persona import Persona
from models.upload import Upload
from models.message import Message
from api.v1.chat import (
    router as chat_router
)
from api.v1.websocket import (
    router as websocket_router
)

from api.v1.chat_sessions import (
    router as chat_session_router
)

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.add_middleware(
    LoggingMiddleware
)
app.add_middleware(
    RateLimitMiddleware
)
app.include_router(
    auth_router,
    prefix="/api/v1/auth",
    tags=["Auth"]
)

app.include_router(
    user_router,
    prefix="/api/v1/users",
    tags=["Users"]
)

app.include_router(
    persona_router,
    prefix="/api/v1/personas",
    tags=["Personas"]
)

app.include_router(
    upload_router,
    prefix="/api/v1/uploads",
    tags=["Uploads"]
)

app.include_router(
    chat_router,
    prefix="/api/v1/chat",
    tags=["Chat"]
)

app.include_router(
    websocket_router,
    prefix="/api/v1/websocket",
    tags=["WebSocket"]
)

app.include_router(
    chat_session_router,
    prefix="/api/v1/chat-sessions",
    tags=["Chat Sessions"]
)