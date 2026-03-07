import numpy as np
import math

def rnn_step_backward(dh, cache):
    """
    Returns:
        dx_t: gradient wrt input x_t      (shape: D,)
        dh_prev: gradient wrt previous h (shape: H,)
        dW: gradient wrt W               (shape: H x D)
        dU: gradient wrt U               (shape: H x H)
        db: gradient wrt bias            (shape: H,)
    """
    x_t = np.array(cache[0])
    h_prev = np.array(cache[1])
    h_t = np.array(cache[2])
    W = np.array(cache[3])
    U = np.array(cache[4])
    b = np.array(cache[5])
    
    dz = dh * ( 1 - (h_t * h_t))

    dx_t = W.T @ dz
    dh_prev = U.T @ dz
    
    dW = np.outer(dz , cache[0])
    dU = np.outer(dz, cache[1])
    
    db = dz

    return (dx_t, dh_prev, dW, dU, db)
    # Write code here
    pass
