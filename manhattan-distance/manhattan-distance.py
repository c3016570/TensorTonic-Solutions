import numpy as np

def manhattan_distance(x, y):
    """
    Compute the Manhattan (L1) distance between vectors x and y.
    Must return a float.
    """
    X = np.array(x)
    Y = np.array(y)
    manhattan_distance = np.linalg.norm(X-Y, ord = 1)
    return manhattan_distance
    pass