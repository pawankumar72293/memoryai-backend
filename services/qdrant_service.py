from qdrant_client import QdrantClient

from qdrant_client.models import (
    Distance,
    VectorParams,
    PointStruct
)


class QdrantService:

    def __init__(self):

        self.client = QdrantClient(
            host="localhost",
            port=6333
        )


    def create_collection(
        self,
        collection_name
    ):

        collections = (
            self.client.get_collections()
        )

        existing = [
            c.name
            for c in collections.collections
        ]

        if collection_name in existing:
            return

        self.client.create_collection(
            collection_name=collection_name,

            vectors_config=VectorParams(
                size=384,
                distance=Distance.COSINE
            )
        )


    def insert_vectors(
        self,
        collection_name,
        vectors,
        payloads
    ):

        points = []

        for index, vector in enumerate(vectors):

            points.append(

                PointStruct(
                    id=index,

                    vector=vector,

                    payload=payloads[index]
                )
            )

        self.client.upsert(
            collection_name=collection_name,
            points=points
        )


    def search(
        self,
        collection_name,
        vector
    ):

        results = self.client.search(
            collection_name=collection_name,

            query_vector=vector,

            limit=10
        )

        return results