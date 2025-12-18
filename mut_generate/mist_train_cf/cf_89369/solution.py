"""
QUESTION:
Write a function `longest_common_subsequence(str1, str2)` that finds the longest common subsequence of two strings, `str1` and `str2`, considering case sensitivity and whitespace. The input strings may contain leading or trailing whitespace, special characters, multiple consecutive whitespace characters, and can be up to 10^4 characters long. The function should return the longest common subsequence of `str1` and `str2`.
"""

def longest_common_subsequence(str1, str2):
    # Remove leading and trailing whitespace
    str1 = str1.strip()
    str2 = str2.strip()
    
    # Initialize a matrix to store the lengths of common subsequences
    matrix = [[0] * (len(str2) + 1) for _ in range(len(str1) + 1)]
    
    # Iterate over the characters of str1 and str2
    for i in range(1, len(str1) + 1):
        for j in range(1, len(str2) + 1):
            # If the characters are the same, increase the length of the common subsequence
            if str1[i - 1] == str2[j - 1]:
                matrix[i][j] = matrix[i - 1][j - 1] + 1
            # If the characters are different, take the maximum of the lengths of previous common subsequences
            else:
                matrix[i][j] = max(matrix[i - 1][j], matrix[i][j - 1])
    
    # Traverse the matrix to construct the longest common subsequence
    subsequence = ""
    i, j = len(str1), len(str2)
    while i > 0 and j > 0:
        # If the characters are the same, append the character to the subsequence and move diagonally up-left
        if str1[i - 1] == str2[j - 1]:
            subsequence = str1[i - 1] + subsequence
            i -= 1
            j -= 1
        # If the characters are different, move to the maximum adjacent cell
        elif matrix[i - 1][j] > matrix[i][j - 1]:
            i -= 1
        else:
            j -= 1
    
    return subsequence