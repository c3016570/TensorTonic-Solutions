import numpy as np
from collections import Counter
import math

def tfidf_vectorizer(documents):
    """
    Build TF-IDF matrix from a list of text documents.
    Returns tuple of (tfidf_matrix, vocabulary).
    """
    if not documents:
        return np.array([]), []

    # build vocabulary
    vocabulary = sorted(set(
        word for doc in documents for word in doc.split() 
    ))

    vocab_index = {word: i for i, word in enumerate(vocabulary)}
    
    N = len(documents)

    # Compute DF
    df = Counter()
    for doc in documents:
        df.update(set(doc.split()))

    tfidf_matrix = []
    
    for document in documents:
        words = document.split()

        # empty document case
        if len(words) == 0:
            tfidf_matrix.append([0]*len(vocabulary))
            continue

        tf_count = Counter(words)

        vector = [0] * len(vocabulary)
        
        for word,count in tf_count.items():
            tf = count / len(words)

        # prevent division by zero in IDF
            if df[word] == 0:
                idf = 0
            else:
                idf = math.log(N/df[word])

            vector[vocab_index[word]] = tf * idf

        tfidf_matrix.append(vector)

    return tfidf_matrix, vocabulary