def text_chunking(tokens, chunk_size, overlap):
    array = []

    if not tokens:
        return []
        
    if len(tokens) <= chunk_size:
        return [tokens]
        
    step = chunk_size - overlap
    
    for i in range(0, len(tokens), step):
        if i + chunk_size > len(tokens):
            break
            
        chunk = tokens[i:i+chunk_size]
        array.append(chunk)
        
    return array            
        
    """
    Split tokens into fixed-size chunks with optional overlap.
    """
    # Write code here