"""
QUESTION:
Write a function `find_max_common_subsequence(string1, string2)` that finds the maximum length common subsequence with the highest frequency of occurrence in both input strings. The function should return the subsequence as a string. The function should not take any additional parameters other than the two input strings. The function should handle strings of any length and any characters.
"""

def find_max_common_subsequence(string1, string2):
    m = len(string1)
    n = len(string2)
    
    # Create a matrix to store the lengths of the common subsequences
    matrix = [[0] * (n+1) for _ in range(m+1)]
    
    # Iterate through the characters of both strings
    for i in range(1, m+1):
        for j in range(1, n+1):
            if string1[i-1] == string2[j-1]:
                # If the characters are equal, add 1 to the length of the previous common subsequence
                matrix[i][j] = matrix[i-1][j-1] + 1
            else:
                # If the characters are different, take the maximum of the previous lengths
                matrix[i][j] = max(matrix[i-1][j], matrix[i][j-1])
    
    # Find the maximum length of the common subsequence
    max_length = matrix[m][n]
    
    # Find the subsequence with the highest frequency of occurrence
    subsequence = ""
    i = m
    j = n
    while i > 0 and j > 0:
        if string1[i-1] == string2[j-1]:
            subsequence = string1[i-1] + subsequence
            i -= 1
            j -= 1
        elif matrix[i-1][j] > matrix[i][j-1]:
            i -= 1
        else:
            j -= 1
    
    return subsequence