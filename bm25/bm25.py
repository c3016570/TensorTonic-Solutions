import numpy as np
from collections import Counter
import math

def bm25_score(query_tokens, docs, k1=1.2, b=0.75):
    """
    Returns numpy array of BM25 scores for each document.
    """
    if len(docs) == 0:
        return np.array([])
    N = len(docs)
    avgdl = sum(len(doc) for doc in docs) / N

    # Compute document frequency for each query term
    df = {}
    for token in query_tokens:
        #dft = [token for doc in docs for token in doc]
        df[token] = sum(1 for doc in docs if token in doc)

    scores = []
    for doc in docs:
        tf = Counter(doc)
        score = 0
        doc_len = len(doc)

        for token in query_tokens:
            if token not in tf:
                continue
    
            idft = math.log(((N - df[token] + 0.5) / (df[token] + 0.5)) + 1 )
            numerator = tf[token] * (k1 + 1)
            denominator = tf[token] + k1 * (1 - b + b * (doc_len / avgdl))
            score += idft * (numerator/denominator)

        scores.append(score)

    return np.array(scores)
    
    # Write code here
    pass