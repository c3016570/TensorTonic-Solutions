from collections import Counter
def bigram_probabilities(tokens):
    """
    Returns: (counts, probs)
      counts: dict mapping (w1, w2) -> integer count
      probs: dict mapping (w1, w2) -> float P(w2 | w1) with add-1 smoothing
    """
    V = sorted(set(tokens))
    vocab_dict = {word: i for i, word in enumerate(V)}

    d_unigrams = Counter(tokens)
    
    tokens_bigrams = [(tokens[i],tokens[i+1]) for i in range(len(tokens)-1)]

    d_bigrams = Counter(tokens_bigrams)

    # count how many bigrams start with w1
    start_counts = Counter()
    for w1, w2 in tokens_bigrams:
        start_counts[w1] = start_counts[w1] + 1 

    probs = {}
    
    for w1 in V:
        for w2 in V:
            bigram_count = d_bigrams[(w1,w2)]
            start_count = start_counts[w1]
            
            prob = (bigram_count + 1)/(start_count + len(V))    
            probs[(w1,w2)] = prob
            
    return d_bigrams,probs
    # Your code here
