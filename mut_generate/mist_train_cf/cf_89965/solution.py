"""
QUESTION:
Implement a function `longest_common_subsequence(string1, string2)` that finds the longest common subsequence of two input strings `string1` and `string2`. The function should return the longest common subsequence as a string. The implementation should use dynamic programming with a matrix to store intermediate results and have a time complexity of O(n^2), where n is the length of the longest string. The function should handle any printable ASCII characters, including special characters and whitespace, and should be memory efficient, using no more than O(n^2) space.
"""

def longest_common_subsequence(string1, string2):
    m = len(string1)
    n = len(string2)

    # Create the matrix
    matrix = [[0] * (n+1) for _ in range(m+1)]

    # Fill the matrix
    for i in range(1, m+1):
        for j in range(1, n+1):
            if string1[i-1] == string2[j-1]:
                matrix[i][j] = matrix[i-1][j-1] + 1
            else:
                matrix[i][j] = max(matrix[i-1][j], matrix[i][j-1])

    # Backtrack to construct the subsequence
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