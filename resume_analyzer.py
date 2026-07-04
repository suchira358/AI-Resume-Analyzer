from resume_parser import extract_text
from skill_extractor import extract_skills
from similarity import calculate_similarity
from ats_score import calculate_ats_score
from feedback import generate_feedback

from career_recommender import recommend_roles
from role_fit import role_fit
from career_guidance import generate_guidance, detect_target_role


def analyze_resume(resume_file, job_description):

    # Extract resume text
    resume_text = extract_text(resume_file)

    # Extract skills
    resume_skills = extract_skills(resume_text)
    job_skills = extract_skills(job_description)

    # Matched skills
    matched_skills = sorted(
        list(set(resume_skills) & set(job_skills))
    )

    # Missing skills
    missing_skills = sorted(
        list(set(job_skills) - set(resume_skills))
    )

    # Semantic similarity
    semantic_similarity = calculate_similarity(
        resume_text,
        job_description
    )

    # Skill match %
    if len(job_skills) > 0:
        skill_match = (
            len(matched_skills) /
            len(job_skills)
        ) * 100
    else:
        skill_match = 0

    # Final similarity
    final_similarity = (
        semantic_similarity * 0.4 +
        skill_match * 0.6
    )

    # ATS Score
    score = calculate_ats_score(
        final_similarity,
        matched_skills,
        missing_skills,
        resume_text
    )

    # Feedback
    feedback = generate_feedback(
        score,
        missing_skills
    )

    # Role Fit
    fit, reason = role_fit(score)

    # Recommended Roles
    recommended_roles = recommend_roles(
        resume_skills
    )

    # Detect target role from JD
    target_role = detect_target_role(
        job_description
    )

    # Default values
    show_recommendations = True
    show_guidance = True

    # CASE 1:
    # User already belongs to same domain
    if (
        recommended_roles and
        recommended_roles[0][0] == target_role
    ):

        reason = (
            f"Your profile aligns well with the "
            f"{target_role} role. "
            f"To improve your chances of getting "
            f"shortlisted, focus on these skills: "
            f"{', '.join(missing_skills)}."
        )
       

        show_recommendations = False
        show_guidance = False

    # CASE 2:
    # Different domain
    else:

        guidance = generate_guidance(
            job_description,
            missing_skills,
            fit
        )

    return {

        "score": round(score),

        "similarity": round(final_similarity),

        "skills": matched_skills,

        "missing_skills": missing_skills,

        "feedback": feedback,

        "role_fit": fit,

        "reason": reason,

        "recommended_roles": recommended_roles,

        "show_recommendations": show_recommendations,

        "show_guidance": show_guidance,

        "guidance": (
            guidance if show_guidance else ""
        )
    }