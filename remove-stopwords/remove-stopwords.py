def remove_stopwords(tokens, stopwords):
    """
    Returns: list[str] - tokens with stopwords removed (preserve order)
    """
    result = []
    for i in range(len(tokens)):
        if tokens[i] not in stopwords:
            result.append(tokens[i])
    return result# Your code here
    pass