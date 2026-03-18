import json
import faiss
import numpy as np
from backend.rag.embedder import embed_text

with open("data/skills_db.json") as f:
    skills_db = json.load(f)

skill_store = []

for domain in skills_db:
    skill_store.extend(skills_db[domain])

vectors = [embed_text(skill) for skill in skill_store]

dimension = len(vectors[0])

index = faiss.IndexFlatL2(dimension)

index.add(np.array(vectors).astype("float32"))