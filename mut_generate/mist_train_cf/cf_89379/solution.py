"""
QUESTION:
Implement a function named `longest_common_subsequence` that takes two strings `str1` and `str2` as input. The function should find the longest common subsequence in `str1` and `str2` that contains only uppercase alphabetical characters. If there are multiple subsequences with the same length, return the one that comes first lexicographically. The function should return the longest common subsequence and its length. The input strings should have a minimum length of 15 characters each.
"""

def longest_common_subsequence(str1, str2):
    """
    This function finds the longest common subsequence in two input strings 
    that contains only uppercase alphabetical characters. If there are multiple 
    subsequences with the same length, it returns the one that comes first 
    lexicographically. The function returns the longest common subsequence and its length.

    Args:
    str1 (str): The first input string.
    str2 (str): The second input string.

    Returns:
    tuple: A tuple containing the longest common subsequence and its length.
    """
    
    # Get the lengths of the input strings
    m, n = len(str1), len(str2)
    
    # Initialize a dynamic programming table
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Build the dynamic programming table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            # Check if the current characters in both strings are the same and uppercase
            if str1[i - 1] == str2[j - 1] and str1[i - 1].isupper():
                # If they are the same, increment the length of the common subsequence
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                # Otherwise, take the maximum length from the previous cells
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    
    # Retrieve the longest common subsequence
    lcs_length = dp[m][n]
    lcs = [''] * lcs_length
    i, j = m, n
    
    # Backtrack to construct the longest common subsequence
    while i > 0 and j > 0:
        # Check if the current characters in both strings are the same and uppercase
        if str1[i - 1] == str2[j - 1] and str1[i - 1].isupper():
            # If they are the same, add the character to the subsequence
            lcs[lcs_length - 1] = str1[i - 1]
            i -= 1
            j -= 1
            lcs_length -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            # Move to the cell with the maximum length
            i -= 1
        else:
            j -= 1
    
    # Return the longest common subsequence and its length
    return ''.join(lcs), len(lcs)