# src/matching.py
from sentence_transformers import SentenceTransformer, util

# Load a pre-trained model once when the module is imported for efficiency.
similarity_model = SentenceTransformer('all-mpnet-base-v2')

def calculate_semantic_similarity(text1: str, text2: str) -> float:
    """
    Calculates the cosine similarity between two texts using a sentence-transformer model.

    Args:
        text1: The first piece of text.
        text2: The second piece of text.

    Returns:
        A similarity score between 0 and 1.
    """
    if not text1 or not text2:
        return 0.0

    # Encode texts into high-dimensional vectors
    embedding1 = similarity_model.encode(text1, convert_to_tensor=True)
    embedding2 = similarity_model.encode(text2, convert_to_tensor=True)

    # Compute cosine similarity
    cosine_score = util.pytorch_cos_sim(embedding1, embedding2)
    
    #.item() extracts the value from the tensor
    return cosine_score.item()
