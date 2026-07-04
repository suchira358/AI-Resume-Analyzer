from career_recommender import ROLE_SKILLS


def detect_target_role(job_description):

    job = job_description.lower()

    best_role = "this role"
    best_score = 0

    for role, skills in ROLE_SKILLS.items():

        score = 0

        for skill in skills:

            if skill in job:
                score += 1

        if score > best_score:
            best_score = score
            best_role = role

    return best_role


def generate_guidance(job_description,
                      missing_skills,
                      role_fit):

    role = detect_target_role(job_description)

    if not missing_skills:

        return (
            f"Your profile is well aligned with the {role} role."
        )

    skills = ", ".join(
        skill.title() for skill in missing_skills
    )

    if role_fit == "Excellent Match":

        return (
            f"To become an even stronger {role}, "
            f"you should learn these skills: {skills}."
        )

    elif role_fit == "Good Match":

        return (
            f"You are a good match for the {role} role. "
            f"Learning these skills will strengthen your profile: {skills}."
        )

    elif role_fit == "Moderate Match":

        return (
            f"If you are aiming for the {role} role, "
            f"you should learn these skills: {skills}."
        )

    else:

        return (
            f"Your profile is better suited for another domain. "
            f"If you want to pursue the {role} role, "
            f"you should learn these skills: {skills}."
        )