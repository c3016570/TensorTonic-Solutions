import numpy as np
import math

def detect_skew(train_dist, serving_dist, threshold=0.2, eps=1e-10):
    """
    Detect train-serving skew using PSI.
    """
    output = {}
    
    for key, value in train_dist.items():
        d = {}
        psi_total = 0

        for v in range(len(value)):
            p_prod = serving_dist[key][v] + eps
            p_train = train_dist[key][v] + eps
            sub = p_prod - p_train
            div = math.log(float(p_prod/p_train))

            psi_total = psi_total + (sub * div)
            if psi_total >= threshold:
                skewed = True
            else:
                skewed = False
            d["psi"] = psi_total
            d["skewed"] = skewed

        output[key] = d

    return output
    # Write code here
    pass