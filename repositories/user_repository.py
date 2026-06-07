from models.user import User


class UserRepository:

    def get_by_email(
        self,
        db,
        email
    ):
        return (
            db.query(User)
            .filter(User.email == email)
            .first()
        )

    def create(
        self,
        db,
        data
    ):

        user = User(**data)

        db.add(user)

        db.commit()

        db.refresh(user)

        return user