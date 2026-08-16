import torch
import torch.nn.functional as F
import math

def scaled_dot_product_attention(Q: torch.Tensor, K: torch.Tensor, V: torch.Tensor) -> torch.Tensor:
    """
    Compute scaled dot-product attention.
    """
    raw_scores = torch.matmul( Q, K.transpose(-2,-1))
    d_k = K.shape[-1]
    scaled_dot_product = raw_scores / math.sqrt(d_k)
    attention_weights = F.softmax(scaled_dot_product, dim = -1) 
    attention = torch.matmul(attention_weights,V)
    return attention
    
    