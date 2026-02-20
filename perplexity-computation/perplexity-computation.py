import math
def perplexity(prob_distributions, actual_tokens):
    num = len(prob_distributions)
    sum = 0
    for i in range(num):
        p = prob_distributions[i][actual_tokens[i]]
        sum += math.log(p)
    negativeSum = -sum
    exponential = math.exp(float(negativeSum/num))
    return exponential
    
    
    
                    
    """
    Compute the perplexity of a token sequence given predicted distributions.
    """
    # Write code here