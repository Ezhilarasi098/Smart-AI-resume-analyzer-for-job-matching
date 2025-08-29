import nltk
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

stop_words = set(stopwords.words('english'))

def clean_text(text):
    words = nltk.word_tokenize(text)
    words = [w.lower() for w in words if w.isalnum() and w not in stop_words]
    return ' '.join(words)

def match_resume_to_job(resume_text, job_desc):
    resume_clean = clean_text(resume_text)
    job_clean = clean_text(job_desc)

    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform([resume_clean, job_clean])
    similarity = cosine_similarity(vectors[0:1], vectors[1:2])

    return round(similarity[0][0] * 100, 2)
