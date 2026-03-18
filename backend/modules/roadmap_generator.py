def generate_roadmap(missing_skills):

    roadmap = []

    for skill in missing_skills[:10]:

        if len(skill.split()) == 1 and len(skill) < 4:
            continue

        roadmap.append({
            "skill": skill,
            "courses": [f"Learn {skill} fundamentals"],
            "youtube": [f"{skill} tutorial"],
            "projects": [f"Build a small project using {skill}"]
        })

    return roadmap