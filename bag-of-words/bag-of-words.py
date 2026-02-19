import numpy as np

def bag_of_words_vector(tokens, vocab):
    num = len(vocab)
    count = [0]*num
    for i in range(len(vocab)):
        for j in range(len(tokens)):
            if(vocab[i] == tokens[j]):
                count[i] += 1  
    return np.array(count, dtype = int)
    """
    Returns: np.ndarray of shape (len(vocab),), dtype=int
    """
    # Your code here
    pass