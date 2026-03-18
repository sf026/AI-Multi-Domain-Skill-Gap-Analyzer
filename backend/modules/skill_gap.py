def analyze_skill_gap(resume_skills, job_skills):

    matching = list(set(resume_skills) & set(job_skills))

    missing = list(set(job_skills) - set(resume_skills))

    score = (len(matching) / len(job_skills)) * 100

    return matching, missing, score