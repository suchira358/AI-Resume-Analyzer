def role_fit(score):

    if score >= 85:

        return (
            "Excellent Match",
            "Your resume closely matches the requirements of this role."
        )

    elif score >= 70:

        return (
            "Good Match",
            "Your profile matches most of the required skills."
        )

    elif score >= 50:

        return (
            "Moderate Match",
            "Your resume contains some relevant skills, but it is stronger in another technical domain."
        )

    else:

        return (
            "Low Match",
            "Your resume is better suited for another domain than the selected role."
        )