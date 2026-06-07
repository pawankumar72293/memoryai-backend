from models.upload import Upload


class UploadRepository:

    def create(
        self,
        db,
        upload
    ):

        db.add(upload)

        db.commit()

        db.refresh(upload)

        return upload