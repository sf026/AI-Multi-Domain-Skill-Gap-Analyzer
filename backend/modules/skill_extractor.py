import json

def extract_skills(text, domain):

    with open("data/skills_db.json") as f:
        skills_db = json.load(f)

    domain_skills = skills_db.get(domain, [])

    text = text.lower()

    found = []

    for skill in domain_skills:
        words = skill.split()

        for word in words:
            if word in text:
                found.append(skill)
                break

    return list(set(found))