"""
QUESTION:
Implement a function `lcs` that takes two strings `str1` and `str2` as input and returns the longest common subsequence. The function should also be modifiable to find the number of such longest common subsequences. The length of the input strings will not exceed 1000 characters.
"""

def lcs(str1, str2):
    """
    This function calculates the longest common subsequence of two input strings.

    Args:
    str1 (str): The first input string.
    str2 (str): The second input string.

    Returns:
    str: The longest common subsequence of str1 and str2.
    """
    m = len(str1)
    n = len(str2)
    
    matrix = [[0 for _ in range(n+1)] for _ in range(m+1)]
    for i in range(m+1):
        for j in range(n+1):
            if i == 0 or j == 0:
                matrix[i][j] = 0
            elif str1[i-1] == str2[j-1]:
                matrix[i][j] = matrix[i-1][j-1] + 1
            else:
                matrix[i][j] = max(matrix[i-1][j], matrix[i][j-1])
    
    index = matrix[m][n]
    lcs = [''] * (index+1)
    lcs[index] = ''
    
    i = m
    j = n
    while i > 0 and j > 0:
        if str1[i-1] == str2[j-1]:
            lcs[index-1] = str1[i-1]
            i -= 1
            j -= 1
            index -= 1
        elif matrix[i-1][j] > matrix[i][j-1]:
            i -= 1
        else:
            j -= 1
    return ''.join(lcs)