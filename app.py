import streamlit as st
from parser import extract_text_from_pdf
from utils import extract_skills
from utils import clean_text
from utils import recommend_jobs
from utils import calculate_match_score
from utils import find_missing_skills

st.set_page_config(page_title="AI Resume Screening")

st.markdown("""
<style>
.stApp {
    background-color: #F5F7FA;
}
</style>
""", unsafe_allow_html=True)

st.title("🤖 AI Resume Screening & Job Recommendation System")
st.write(
    """
    This AI system analyzes resumes,
    extracts skills,
    calculates job match scores,
    and recommends suitable job roles.
    """
)
st.sidebar.title("AI Resume Screening")
st.sidebar.info("""
Upload your resume and get:
✅ Skill Analysis
✅ Job Recommendations
✅ Match Score
""")

uploaded_file=st.file_uploader("upload Resume (PDF)",type=["pdf"])
if uploaded_file is not None:
    text=extract_text_from_pdf(uploaded_file)
    cleaned_text = clean_text(text)
    st.success("Resume uploaded successfully")

    with st.expander("📄 View Extracted Resume Text"):
     st.write(text)
    skills=extract_skills(text)

    st.header("✅ Skills Found")
    for skill in skills:
        st.write("✅",skill)

    with st.expander("🧹 View Cleaned Resume Text"):
     st.write(cleaned_text)

    job_skills = [
    "Python",
    "SQL",
    "Machine Learning",
    "Power BI"]

    jobs = recommend_jobs(skills)
    st.header("💼 Recommended Jobs")
    for job in jobs:
      st.success(job)   

    score = calculate_match_score(skills,job_skills)
    st.header("🎯 Match Score")
    st.write(f"{score}%")

    if score >= 80:
     st.success("🌟 Strong Resume")
    elif score >= 60:
     st.info("👍 Good Resume")
    else:
     st.warning("📚 Needs Improvement")

    missing_skills = find_missing_skills(
    skills,
    job_skills)

    st.subheader("❌ Missing Skills")
    if missing_skills:
     for skill in missing_skills:
        st.warning(skill)
    else:
     st.success("No Missing Skills Found!")
    st.header("📊 Resume Analysis Dashboard")
    col1, col2, col3 = st.columns(3)
    with col1:
      st.metric("Skills Found", len(skills))
    with col2:
      st.metric("Recommended Jobs", len(jobs))
    with col3:
      st.metric("Match Score", f"{score}%")


    st.progress(score/100)
    

    report = f"""
Skills Found:
{skills}

Recommended Jobs:
{jobs}

Match Score:
{score}%

Missing Skills:
{missing_skills}
"""

    st.download_button(
        label="📥 Download Report",
        data=report,
        file_name="resume_analysis_report.txt",
        mime="text/plain"
    )

st.markdown("---")

st.markdown("""
### 👩‍💻 Developer
**Gayathri Parthipan**

AI Resume Screening & Job Recommendation System

Built using Python, Streamlit, NLP, and PyPDF2.
""")