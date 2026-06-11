def extract_skills(text):
    skills_db=[
    "Python",
    "SQL",
    "HTML",
    "C",
    "C++",
    "Excel",
    "Power BI",
    "Pandas",
    "Numpy",
    "Matplotlib",
    "MySQL",
    "Communication",
    "Leadership",
    "Problem Solving",
    "Time Management",
    "Jupyter Notebook",
    "Google Colab",
    "java"
]
    found_skills = []
    for skill in skills_db:
        if skill.lower() in text.lower():
            found_skills.append(skill)
    return found_skills 

import re
def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    return text
    
def recommend_jobs(skills):

    jobs = []
    if "Python" in skills:
        jobs.append("Python Developer")
    if "SQL" in skills:
        jobs.append("Data Analyst")
    if "Machine Learning" in skills:
        jobs.append("Machine Learning Engineer")
    if "Java" in skills:
        jobs.append("Java Developer")
    if "HTML" in skills or "CSS" in skills or "JavaScript" in skills:
        jobs.append("Frontend Developer")
    return jobs   

def calculate_match_score(resume_skills, job_skills):
    matched_skills = 0
    for skill in resume_skills:
        if skill.lower() in [s.lower() for s in job_skills]:
            matched_skills += 1
    score = (matched_skills / len(job_skills)) * 100
    return round(score, 2)

def find_missing_skills(resume_skills, job_skills):
    missing_skills = []
    for skill in job_skills:
       if skill.lower() not in [s.lower() for s in resume_skills]:
            missing_skills.append(skill)
    return missing_skills