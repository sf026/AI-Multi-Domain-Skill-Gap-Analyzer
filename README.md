# 🤖 AI Multi-Domain Skill Gap Analyzer

An AI-powered web application that analyzes resumes, detects profession, compares with job descriptions, and identifies skill gaps with personalized learning recommendations.

---

## 🚀 Features

- 📄 Upload Resume (PDF/DOCX)
- 🧠 Detect Profession automatically
- 📌 Upload or Paste Job Description
- 📊 Skill Matching Score Calculation
- ✅ Matching Skills Identification
- ❌ Missing Skills Detection
- ✍️ Resume Improvement Suggestions
- 🧭 AI Learning Roadmap (Courses, YouTube, Projects)

---

## 🏗️ System Architecture
Frontend (Streamlit)
↓
Backend (FastAPI)
↓
NLP + RAG Processing
↓
Skill Gap Analysis Output


---

## 🧠 How It Works

1. User uploads resume
2. System extracts text from resume
3. Job description is provided (text/file)
4. Profession is detected using NLP
5. Skills are extracted from both resume & job description
6. Matching score is calculated
7. Missing skills are identified
8. AI generates improvement suggestions & roadmap

---

## 🔍 RAG (Retrieval-Augmented Generation)

This project uses RAG principles:

- 📚 Retrieval: Skills and occupation data from dataset
- 🤖 Generation: AI generates insights, improvements, roadmap
- 🎯 Combines structured data + LLM output

---

## 💻 Tech Stack

- **Frontend:** Streamlit
- **Backend:** FastAPI
- **Language:** Python
- **Libraries:**
  - PyPDF / docx
  - Pandas
  - NLP processing
  - OpenAI API (for AI insights)

---
## 📊 Output Example

- Profession: Teacher
- Matching Score: 41%
- Matching Skills: List
- Missing Skills: List
- Resume Improvements: Suggestions
- AI Roadmap: Courses + Projects

## ⚠️ Limitations

- Accuracy depends on resume quality
- Limited dataset coverage
- AI responses may vary
- No real-time job market integration


