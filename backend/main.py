from fastapi import FastAPI, UploadFile, File, Form
from typing import Optional

from backend.modules.resume_parser import parse_resume
from backend.modules.ai_skill_extractor import extract_skills
from backend.modules.ai_skill_matcher import match_skills
from backend.modules.resume_improver import resume_improver
from backend.modules.roadmap_generator import generate_roadmap
from backend.modules.profession_detector import detect_profession, get_expected_skills

# ✅ CREATE APP FIRST
app = FastAPI()


@app.get("/")
def home():
    return {"message": "AI Multi-Domain Skill Gap Analyzer API Running"}


@app.post("/analyze")
async def analyze(
    resume: UploadFile = File(...),
    jd_text: Optional[str] = Form(None),
    jd_file: Optional[UploadFile] = File(None)
):

    # ---------- RESUME ----------
    resume_text = parse_resume(resume)

    # ---------- JOB DESCRIPTION ----------
    if jd_file is not None:
        jd_text = parse_resume(jd_file)

    if not jd_text:
        return {"error": "Job description required"}

    # ---------- PROCESS ----------
    resume_skills = extract_skills(resume_text)

    profession = detect_profession(resume_text)
    expected_skills = get_expected_skills(profession)

    matching, missing, score = match_skills(resume_skills, expected_skills)

    improvements = resume_improver(missing)
    roadmap = generate_roadmap(missing)

    return {
        "detected_profession": profession,
        "matching_score": score,
        "matching_skills": matching,
        "missing_skills": missing,
        "resume_improvements": improvements,
        "learning_roadmap": roadmap
    }