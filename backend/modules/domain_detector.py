import json

def detect_domain(text):

    with open("data/skills_db.json") as f:
        skills_db = json.load(f)

    text = text.lower()

    domain_scores = {}

    for domain, skills in skills_db.items():

        score = 0

        for skill in skills:
            if skill in text:
                score += 1

        domain_scores[domain] = score

    return max(domain_scores, key=domain_scores.get)