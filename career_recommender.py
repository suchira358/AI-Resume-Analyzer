ROLE_SKILLS = {

    "Software Engineer": [
        "java", "python", "c++", "sql", "git",
        "html", "css", "javascript",
        "oop", "data structures",
        "algorithms", "rest api",
        "debugging", "testing", "sdlc"
    ],

    "Machine Learning Engineer": [
        "python", "machine learning", "deep learning",
        "tensorflow", "keras", "pytorch",
        "scikit-learn", "numpy", "pandas",
        "statistics", "feature engineering",
        "computer vision", "nlp"
    ],

    "Data Scientist": [
        "python", "sql", "machine learning",
        "statistics", "numpy", "pandas",
        "data analysis", "data visualization",
        "scikit-learn"
    ],

    "Data Analyst": [
        "sql", "excel", "power bi",
        "tableau", "python",
        "statistics", "data analysis",
        "data visualization"
    ],

    "Frontend Developer": [
        "html", "css", "javascript",
        "react", "bootstrap",
        "tailwind css"
    ],

    "Backend Developer": [
        "python", "java", "sql",
        "rest api", "flask",
        "django", "node.js"
    ],

    "Full Stack Developer": [
        "html", "css", "javascript",
        "react", "node.js",
        "express.js", "mongodb",
        "sql", "git"
    ],

    "Cloud Engineer": [
        "aws", "azure",
        "docker", "kubernetes",
        "linux", "git"
    ]
}


def recommend_roles(resume_skills):

    scores = {}

    for role, skills in ROLE_SKILLS.items():

        matched = len(set(resume_skills) & set(skills))

        score = round((matched / len(skills)) * 100)

        scores[role] = score

    recommendations = sorted(
        scores.items(),
        key=lambda x: x[1],
        reverse=True
    )

    return recommendations[:3]