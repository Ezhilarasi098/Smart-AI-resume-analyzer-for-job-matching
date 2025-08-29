import streamlit as st
from resume_parser import extract_text_from_pdf
from match_score import match_resume_to_job
import nltk

nltk.download('punkt')
nltk.download('stopwords')

st.title("📄 Smart Resume Analyzer")

resume_file = st.file_uploader("Upload Your Resume (PDF)", type=["pdf"])
job_description = st.text_area("Paste the Job Description Here")

if st.button("Analyze Match"):

    if resume_file and job_description.strip():
        with st.spinner("Analyzing..."):
            resume_text = extract_text_from_pdf(resume_file)
            score = match_resume_to_job(resume_text, job_description)
            st.success(f"✅ Match Score: {score}%")

            if score > 80:
                st.info("Great match! 🎯")
            elif score > 50:
                st.warning("Partial match. Consider improving your resume.")
            else:
                st.error("Low match. You may want to add more relevant skills.")
    else:
        st.warning("Please upload a resume and paste a job description.")
