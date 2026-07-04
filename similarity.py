from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# Load the model only once
model = SentenceTransformer("all-MiniLM-L6-v2")

def calculate_similarity(resume_text, job_description):
    # Convert text into embeddings
    resume_embedding = model.encode([resume_text])
    job_embedding = model.encode([job_description])

    # Calculate cosine similarity
    similarity = cosine_similarity(
        resume_embedding,
        job_embedding
    )[0][0]

    return round(similarity * 100, 2)