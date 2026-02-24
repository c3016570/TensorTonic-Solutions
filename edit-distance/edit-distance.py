def edit_distance(s1, s2):
    """
    Compute the minimum edit distance between two strings.
    """
    num1 = len(s1)
    num2 = len(s2)
    array = [[0] * (num2 + 1) for _ in range(num1 + 1)]
    
    for i in range(num1 + 1):
        array[i][0] = i
        
    for j in range(num2 + 1):
        array[0][j] = j
        
    for i in range(1, num1 + 1):
        for j in range(1, num2 + 1):
            if s1[i-1] == s2[j-1]:
                array[i][j] = array[i-1][j-1]
            else:
                array[i][j] = 1 + min(array[i-1][j], array[i][j-1], array[i-1][j-1])

    return array[num1][num2]
                
            # Write code here