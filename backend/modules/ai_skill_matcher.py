from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer("all-MiniLM-L6-v2")

SIMILARITY_THRESHOLD = 0.7


def match_skills(resume_skills, jd_skills):

    if not jd_skills:
        return [], [], 0

    if not resume_skills:
        return [], jd_skills, 0

    resume_embeddings = model.encode(resume_skills)
    jd_embeddings = model.encode(jd_skills)

    matching = []
    missing = []

    for i, jd_skill in enumerate(jd_skills):

        similarity_scores = cosine_similarity(
            [jd_embeddings[i]], resume_embeddings
        )[0]

        best_score = max(similarity_scores)

        if best_score >= SIMILARITY_THRESHOLD:
            matching.append(jd_skill)
        else:
            missing.append(jd_skill)

    score = round((len(matching) / len(jd_skills)) * 100, 2)

    return matching, missing, score