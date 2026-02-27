import numpy as np

def pad_sequences(seqs, pad_value=0, max_len=None):
    """
    Returns: np.ndarray of shape (N, L) where:
      N = len(seqs)
      L = max_len if provided else max(len(seq) for seq in seqs) or 0
    """
    if not seqs:
        return np.array([]).reshape(0,0)
        
    if max_len is not None:
        L = max_len
    else:
        L = max(len(seq) for seq in seqs) if seqs else 0

    N = len(seqs)
    padded = np.full((N,L), pad_value, dtype = int)

    # Copy sequences into padded array
    for i, seq in enumerate(seqs):
        # truncate if greater than max_length
        length = min(len(seq), L)
        padded[i,:length] = seq[:length]
        
    return padded
    # Your code here
    pass