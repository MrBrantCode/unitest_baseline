"""
QUESTION:
Implement a function `longest_common_subsequence(str1, str2)` to find the longest common subsequence between two strings. The subsequence should only contain alphabetical characters. Both input strings should have a minimum length of 10 characters.
"""

def longest_common_subsequence(str1, str2):
    """
    This function finds the longest common subsequence between two strings.
    The subsequence should only contain alphabetical characters.
    
    Args:
        str1 (str): The first input string.
        str2 (str): The second input string.
    
    Returns:
        str: The longest common subsequence.
    """
    m = len(str1)
    n = len(str2)

    # Creating a matrix to store the lengths of longest common subsequences
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Computing the lengths of LCSs
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1].isalpha() and str2[j - 1].isalpha():
                if str1[i - 1] == str2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # Constructing the LCS from dp matrix
    lcs_length = dp[m][n]
    lcs = [''] * lcs_length
    i = m
    j = n
    while i > 0 and j > 0:
        if str1[i - 1].isalpha() and str2[j - 1].isalpha():
            if str1[i - 1] == str2[j - 1]:
                lcs[lcs_length - 1] = str1[i - 1]
                i -= 1
                j -= 1
                lcs_length -= 1
            elif dp[i - 1][j] > dp[i][j - 1]:
                i -= 1
            else:
                j -= 1
        else:
            if str1[i - 1].isalpha():
                j -= 1
            else:
                i -= 1

    return ''.join(lcs)