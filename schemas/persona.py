from pydantic import BaseModel


class CreatePersonaSchema(BaseModel):

    name: str

    relationship: str

    description: str | None = None