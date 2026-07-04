import re
import pandas as pd

skills_df = pd.read_csv("data/skills.csv")
skill_list = skills_df["Skill"].str.lower().tolist()

def extract_skills(text):
    text = text.lower()
    found = []

    for skill in skill_list:
        pattern = r"\b" + re.escape(skill) + r"s?\b"
        if re.search(pattern, text):
            found.append(skill)

    return sorted(list(set(found)))

def missing_skills(resume_skills, job_description):
    job_skills = extract_skills(job_description)
    return [skill for skill in job_skills if skill not in resume_skills]