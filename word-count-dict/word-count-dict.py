def word_count_dict(sentences):
    """
    Returns: dict[str, int] - global word frequency across all sentences
    """
    d = dict()
    for i in range(len(sentences)):
        num = len(sentences[i])
        for j in range(num):
            key = sentences[i][j]
            if key in d:
                d[key] = d[key] + 1
            else:
                d[key] = 1
    return d
            
            # Your code here
    pass