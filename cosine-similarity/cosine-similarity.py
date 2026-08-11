import numpy as np

def cosine_similarity(a, b):
    """
    Compute cosine similarity between two 1D NumPy arrays.
    Returns: float in [-1, 1]
    """
    A = np.array(a)
    B = np.array(b)
    dot_product = np.dot(A,B)
    norm_a = np.linalg.norm(A)
    norm_b = np.linalg.norm(B)
    denominator = norm_a * norm_b
    if denominator == 0:
        similarity = 0.0
    else:
        similarity = dot_product / (norm_a * norm_b)
    return similarity
    pass