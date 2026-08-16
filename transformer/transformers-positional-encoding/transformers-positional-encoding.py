import numpy as np

def positional_encoding(seq_length: int, d_model: int) -> np.ndarray:
    """
    Generate sinusoidal positional encodings.
    """
    # position indices : (seq_length, 1)
    position = np.arange(seq_length).reshape(-1,1)

    # dimension indices : (1, d_model)
    dimension = np.arange(d_model).reshape(1,-1)

    # compute the angle rates
    angle_rates = 1 / np.power(
        10000, 2 * (dimension//2) / d_model
    )

    # compute angles

    angles = position * angle_rates

    # output initialization
    output = np.zeros((seq_length, d_model))

    # apply sin to even dimensions
    output[:,0::2] = np.sin(angles[:, 0::2])
    # apply cos to odd dimensions
    output[:,1::2] = np.cos(angles[:, 1::2])

    return output