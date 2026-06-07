import faiss
import pickle
import numpy as np


class VectorService:

    def search(
        self,
        persona_id,
        query_embedding,
        k=10
    ):

        index = faiss.read_index(
            f"storage/faiss/{persona_id}.index"
        )

        with open(
            f"storage/faiss/{persona_id}.pkl",
            "rb"
        ) as f:

            message_ids = pickle.load(f)

        query = np.array(
            [query_embedding],
            dtype="float32"
        )

        distances, indices = (
            index.search(
                query,
                k
            )
        )

        result_ids = []

        for idx in indices[0]:

            if idx >= 0:

                result_ids.append(
                    message_ids[idx]
                )

        return result_ids