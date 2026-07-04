import streamlit as st
from resume_analyzer import analyze_resume

# ---------------- Page Configuration ----------------
st.set_page_config(
    page_title="AI Resume ATS Analyzer",
    page_icon="📄",
    layout="wide"
)

# ---------------- Custom CSS ----------------
st.markdown("""
<style>

.main-title{
    text-align:center;
    color:#0E76A8;
    font-size:40px;
    font-weight:bold;
}

.sub{
    text-align:center;
    color:gray;
    font-size:18px;
}

</style>
""", unsafe_allow_html=True)

# ---------------- Title ----------------
st.markdown('<p class="main-title">📄 AI Resume ATS Analyzer</p>', unsafe_allow_html=True)
st.markdown('<p class="sub">Analyze your Resume against a Job Description using AI & NLP</p>', unsafe_allow_html=True)

st.write("")

# ---------------- Input ----------------
resume = st.file_uploader("📂 Upload Resume (PDF)", type=["pdf"])

job_desc = st.text_area("📝 Paste Job Description", height=220)

st.write("")

# ---------------- Analyze ----------------
if st.button("🚀 Analyze Resume", use_container_width=True):

    if resume is None or job_desc.strip() == "":
        st.warning("Please upload a resume and paste the Job Description.")

    else:

        result = analyze_resume(resume, job_desc)

        st.success("Resume Analysis Completed Successfully!")

        st.write("")

        # ---------------- ATS & Similarity (NO BOX UI) ----------------

        col1, col2 = st.columns(2)

        with col1:
            st.markdown("### 🎯 ATS Score")
            st.markdown(f"## {result['score']}%")
            st.progress(int(result["score"]))

        with col2:
            st.markdown("### 📊 Similarity")
            st.markdown(f"## {result['similarity']}%")
            st.progress(int(result["similarity"]))

        st.divider()

        # ---------------- Skills Dashboard ----------------

        col3, col4 = st.columns(2)

        with col3:
            st.subheader("✅ Matched Skills")

            if result["skills"]:
                for skill in result["skills"]:
                    st.success(skill.title())
            else:
                st.info("No matched skills found.")

        with col4:
            st.subheader("❌ Missing Skills")

            if result["missing_skills"]:
                for skill in result["missing_skills"]:
                    st.error(skill.title())
            else:
                st.success("No important skills are missing.")

        st.divider()

        # ---------------- Feedback ----------------

        st.subheader("💡 Feedback")

        for item in result["feedback"]:
            st.info(item)

        st.divider()

        # ---------------- Role Fit ----------------

        st.subheader("🎯 Role Fit")

        if result["role_fit"] == "Excellent Match":
            st.success(result["role_fit"])

        elif result["role_fit"] == "Good Match":
            st.success(result["role_fit"])

        elif result["role_fit"] == "Moderate Match":
            st.warning(result["role_fit"])

        else:
            st.error(result["role_fit"])

        st.write(result["reason"])

        # ---------------- Recommended Roles ----------------

        if result["show_recommendations"]:

            st.divider()
            st.subheader("🚀 Recommended Career Roles")

            medals = ["🥇", "🥈", "🥉"]

            for i, (role, score) in enumerate(result["recommended_roles"]):
                if i < 3:
                    st.write(f"{medals[i]} **{role}** — {score}% Match")
                else:
                    st.write(f"• **{role}** — {score}% Match")

        # ---------------- Career Guidance ----------------

        if result["show_guidance"]:

            st.divider()
            st.subheader("📚 Career Guidance")

            st.info(result["guidance"])