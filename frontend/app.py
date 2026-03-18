import streamlit as st
import requests
import os

st.set_page_config(page_title="AI Skill Gap Analyzer", layout="wide")

# 🎨 CUSTOM CSS (FIXED UI)
st.markdown("""
<style>
.main {
    background-color: #0e1117;
    color: white;
}

.card {
    background-color: #ffffff;
    padding: 20px;
    border-radius: 12px;
    box-shadow: 0px 4px 12px rgba(0,0,0,0.2);
    margin-bottom: 20px;
    color: #000000;
}

.title {
    text-align: center;
    color: #ffffff;
    font-size: 36px;
    font-weight: bold;
}

.section {
    color: #00c6ff;
    font-size: 22px;
    margin-top: 10px;
}
</style>
""", unsafe_allow_html=True)

# 🏷️ TITLE
st.markdown('<p class="title">🚀 AI Multi-Domain Skill Gap Analyzer</p>', unsafe_allow_html=True)

# 📂 UPLOAD SECTION
col1, col2 = st.columns(2)

with col1:
    resume_file = st.file_uploader("📄 Upload Resume (PDF/DOCX)", type=["pdf", "docx"])

with col2:
    jd_file = st.file_uploader("📄 Upload Job Description (Optional)", type=["pdf", "docx"])

# 📝 TEXT INPUT (OPTIONAL)
jd_text_input = st.text_area("✍️ Or Paste Job Description")

# 🚀 ANALYZE BUTTON
if st.button("🔍 Analyze"):

    if resume_file is None:
        st.error("⚠️ Please upload a resume")
    else:
        os.makedirs("uploads", exist_ok=True)

        # SAVE RESUME
        resume_path = os.path.abspath(os.path.join("uploads", resume_file.name))
        with open(resume_path, "wb") as f:
            f.write(resume_file.getbuffer())

        # HANDLE JD INPUT
        jd_text = ""

        if jd_file is not None:
            jd_path = os.path.abspath(os.path.join("uploads", jd_file.name))
            with open(jd_path, "wb") as f:
                f.write(jd_file.getbuffer())

            jd_text = jd_path  # send file path to backend

        elif jd_text_input:
            jd_text = jd_text_input

        else:
            jd_text = ""  # optional case

        try:
            files = {
    "resume": (resume_file.name, resume_file.getvalue())
}

            data = {
    "jd_text": jd_text
}

            response = requests.post(
    "http://127.0.0.1:8000/analyze",
    files=files,
    data=data
)

            if response.status_code != 200:
                st.error(f"❌ Backend Error: {response.text}")
            else:
                data = response.json()

                st.markdown("## 📊 Analysis Result")

                # 🎯 DETECTED PROFESSION
                st.markdown(f"""
                <div class="card">
                    <h3>🎯 Detected Profession</h3>
                    <p>{data.get("detected_profession","N/A")}</p>
                </div>
                """, unsafe_allow_html=True)

                # 📈 MATCH SCORE
                st.markdown(f"""
                <div class="card">
                    <h3>📈 Matching Score</h3>
                    <h2>{data.get("matching_score",0)}%</h2>
                </div>
                """, unsafe_allow_html=True)

                # ✅ MATCHING SKILLS
                st.markdown('<div class="card"><h3>✅ Matching Skills</h3>', unsafe_allow_html=True)
                for skill in data.get("matching_skills", []):
                    st.write(f"✔ {skill}")
                st.markdown('</div>', unsafe_allow_html=True)

                # ❌ MISSING SKILLS
                st.markdown('<div class="card"><h3>❌ Missing Skills</h3>', unsafe_allow_html=True)
                for skill in data.get("missing_skills", []):
                    st.write(f"🔸 {skill}")
                st.markdown('</div>', unsafe_allow_html=True)

                # 🛠️ IMPROVEMENTS
                st.markdown('<div class="card"><h3>🛠️ Resume Improvements</h3>', unsafe_allow_html=True)
                for tip in data.get("resume_improvements", []):
                    st.write(f"👉 {tip}")
                st.markdown('</div>', unsafe_allow_html=True)

                # 📚 LEARNING ROADMAP
                st.markdown('<div class="card"><h3>📚 AI Learning Roadmap</h3>', unsafe_allow_html=True)

                for item in data.get("learning_roadmap", []):
                    st.markdown(f"### 🔹 {item.get('skill','')}")

                    st.write("📘 Courses:")
                    for c in item.get("courses", []):
                        st.write(f"- {c}")

                    st.write("🎥 YouTube:")
                    for y in item.get("youtube", []):
                        st.write(f"- {y}")

                    st.write("💡 Projects:")
                    for p in item.get("projects", []):
                        st.write(f"- {p}")

                    st.markdown("---")

                st.markdown('</div>', unsafe_allow_html=True)

        except Exception as e:
            st.error(f"❌ Connection Error: {e}")