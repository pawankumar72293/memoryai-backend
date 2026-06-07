from pydantic import BaseModel


class ChatSchema(BaseModel):

    persona_id: str

    session_id: str

    message: str