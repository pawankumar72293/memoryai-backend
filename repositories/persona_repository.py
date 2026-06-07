from models.persona import Persona


class PersonaRepository:

    def create(
        self,
        db,
        persona
    ):

        db.add(persona)

        db.commit()

        db.refresh(persona)

        return persona

    def get_all(
        self,
        db,
        user_id
    ):

        return (
            db.query(Persona)
            .filter(Persona.user_id == user_id)
            .all()
        )

    def get_by_id(
        self,
        db,
        persona_id,
        user_id
    ):

        return (
            db.query(Persona)
            .filter(Persona.id == persona_id)
            .filter(Persona.user_id == user_id)
            .first()
        )