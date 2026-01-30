"""
matcher.py
Matches resume text with job description using semantic similarity
"""

from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity


# Load AI model once
model = SentenceTransformer("all-MiniLM-L6-v2")


def calculate_match_score(resume_text: str, job_text: str) -> float:
    """
    Returns match percentage between resume and job description
    """

    embeddings = model.encode([resume_text, job_text])

    similarity = cosine_similarity(
        [embeddings[0]],
        [embeddings[1]]
    )[0][0]

    return round(similarity * 100, 2)
