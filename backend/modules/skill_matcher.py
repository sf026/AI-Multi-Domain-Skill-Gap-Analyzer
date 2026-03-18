def match_skills(resume_skills, jd_skills):
    matching = list(set(resume_skills) & set(jd_skills))
    missing = list(set(jd_skills) - set(resume_skills))
    score = 0
    if len(jd_skills) > 0:
        score = round(len(matching) / len(jd_skills) * 100, 2)
    return matching, missing, score