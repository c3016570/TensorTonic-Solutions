import math
from collections import Counter
def bleu_score(candidate, reference, max_n):
    """
    Compute the BLEU score for a candidate translation.
    """
    r = len(reference)
    c = len(candidate)

    if c == 0:
        return 0

    sum_total_logarithmic = 0
    
    for n in range(1,max_n + 1):

        n_grams_candidate = [
            tuple(candidate[i:i+n]) for i in range(len(candidate) - n + 1)
        ]

        n_grams_reference = [
            tuple(reference[j:j+n]) for j in range(len(reference) - n + 1)
        ]

        # Counting n-grams here

        d_candidate = Counter(n_grams_candidate)
        d_reference = Counter(n_grams_reference)


        sum_numerator = 0
        sum_denominator = sum(d_candidate.values())
        
        for n_gram in d_candidate:
            sum_numerator += min(d_candidate[n_gram],d_reference.get(n_gram,0))

        if sum_denominator == 0:
            return 0

        precision_n_gram = sum_numerator / sum_denominator

        if precision_n_gram == 0:
            return 0
            
        sum_total_logarithmic += math.log(precision_n_gram)    
    
    if c >= r:
        bp = 1
    else:
        bp = math.exp(1 - r/c)
    
    bleu = bp * math.exp(sum_total_logarithmic/max_n)
    
    return bleu# Write code here