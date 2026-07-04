def generate_feedback(score, missing_skills):

    feedback=[]

    if score>=85:
        feedback.append("Excellent ATS-friendly resume.")

    elif score>=70:
        feedback.append("Good resume with minor improvements needed.")

    elif score>=50:
        feedback.append("Average resume. Improve skills and keywords.")

    else:
        feedback.append("Resume needs improvement to pass ATS screening.")

    if missing_skills:

        feedback.append(
            "Missing Skills: "+", ".join(missing_skills)
        )

    else:

        feedback.append(
            "Excellent! All important job skills are present."
        )

    feedback.append(
        "Use action verbs and quantify achievements."
    )

    feedback.append(
        "Keep the resume ATS-friendly with clear headings."
    )

    return feedback