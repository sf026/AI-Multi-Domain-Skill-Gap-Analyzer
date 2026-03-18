import numpy as np
from backend.rag.vector_store import index, skill_store
from backend.rag.embedder import embed_text

def retrieve_similar(text, k=5):

    query_vector = embed_text(text)

    D, I = index.search(
        np.array([query_vector]).astype("float32"), k
    )

    skills = [skill_store[i] for i in I[0]]

    return skills