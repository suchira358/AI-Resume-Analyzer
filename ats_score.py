def calculate_ats_score(similarity, resume_skills, missing_skills, resume_text):

    score = 0

    # Similarity = 50 marks
    score += (similarity / 100) * 50

    # Skills = 30 marks
    total = len(resume_skills) + len(missing_skills)

    if total > 0:
        matched = total - len(missing_skills)
        score += (matched / total) * 30

    # Resume Sections = 20 marks
    sections = [
        "education",
        "skills",
        "projects",
        "experience",
        "certifications"
    ]

    text = resume_text.lower()

    section_score = 0

    for section in sections:
        if section in text:
            section_score += 4

    score += section_score

    return round(min(score,100),2)