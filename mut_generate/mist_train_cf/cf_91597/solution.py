"""
QUESTION:
Write a function `transform_string(str1, str2)` that takes two input strings `str1` and `str2` and returns the minimum number of edits (insertions, deletions, or substitutions) required to transform `str1` into `str2` along with the sequence of edits.
"""

def transform_string(str1, str2):
    m = len(str1)
    n = len(str2)
    
    # Create a matrix to store the distance values
    distance = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Initialize the first row and column
    for i in range(m + 1):
        distance[i][0] = i
    for j in range(n + 1):
        distance[0][j] = j
    
    # Compute the distance matrix
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                distance[i][j] = distance[i - 1][j - 1]
            else:
                distance[i][j] = 1 + min(distance[i - 1][j], distance[i][j - 1], distance[i - 1][j - 1])
    
    # Backtrack to find the sequence of edits
    i, j = m, n
    edits = []
    while i > 0 and j > 0:
        if str1[i - 1] == str2[j - 1]:
            i -= 1
            j -= 1
        elif distance[i][j] == distance[i - 1][j - 1] + 1:
            edits.append(f"Substitute '{str1[i - 1]}' with '{str2[j - 1]}'")
            i -= 1
            j -= 1
        elif distance[i][j] == distance[i - 1][j] + 1:
            edits.append(f"Delete '{str1[i - 1]}'")
            i -= 1
        elif distance[i][j] == distance[i][j - 1] + 1:
            edits.append(f"Insert '{str2[j - 1]}'")
            j -= 1
    
    while i > 0:
        edits.append(f"Delete '{str1[i - 1]}'")
        i -= 1
    
    while j > 0:
        edits.append(f"Insert '{str2[j - 1]}'")
        j -= 1
    
    edits.reverse()
    return len(edits), edits