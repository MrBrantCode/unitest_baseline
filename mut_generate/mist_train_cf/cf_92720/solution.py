"""
QUESTION:
Write a function `longest_common_subsequence(str1, str2)` that finds the longest common subsequence of two input strings `str1` and `str2`. The function should be case sensitive and consider any leading or trailing whitespace. It should return the longest common subsequence as a string, preserving the order of the words and without removing any whitespace within the words.
"""

def longest_common_subsequence(str1, str2):
    # Removing leading and trailing whitespace
    str1 = str1.strip()
    str2 = str2.strip()
    
    # Splitting strings into lists of words
    words1 = str1.split()
    words2 = str2.split()
    
    # Creating a matrix to store the lengths of common subsequences
    matrix = [[0] * (len(words2) + 1) for _ in range(len(words1) + 1)]
    
    # Filling the matrix with lengths of common subsequences
    for i in range(1, len(words1) + 1):
        for j in range(1, len(words2) + 1):
            if words1[i - 1] == words2[j - 1]:
                matrix[i][j] = matrix[i - 1][j - 1] + 1
            else:
                matrix[i][j] = max(matrix[i - 1][j], matrix[i][j - 1])
    
    # Finding the longest common subsequence
    lcs = []
    i, j = len(words1), len(words2)
    while i > 0 and j > 0:
        if words1[i - 1] == words2[j - 1]:
            lcs.append(words1[i - 1])
            i -= 1
            j -= 1
        elif matrix[i - 1][j] > matrix[i][j - 1]:
            i -= 1
        else:
            j -= 1
    
    # Reversing the list to get the correct order
    lcs.reverse()
    
    # Joining the words of the longest common subsequence into a string
    lcs_str = ' '.join(lcs)
    
    return lcs_str