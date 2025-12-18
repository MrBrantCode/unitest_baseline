"""
QUESTION:
Implement a function called "longest_common_substring" that takes two strings as input and returns the longest common substring found between them, ignoring case differences. The function should consider all possible substrings of both strings, return the longest one that appears in both strings, and prioritize the first occurrence in the first string if multiple substrings have the same length. The input strings only contain alphanumeric characters and spaces, have no leading or trailing spaces, and may have different lengths.
"""

def longest_common_substring(s1: str, s2: str) -> str:
    """
    This function finds the longest common substring of two input strings, ignoring case differences.
    
    Parameters:
    s1 (str): The first input string.
    s2 (str): The second input string.
    
    Returns:
    str: The longest common substring found between the two input strings.
    """
    s1 = s1.lower()
    s2 = s2.lower()
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    max_length = 0
    end = 0
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                if dp[i][j] > max_length:
                    max_length = dp[i][j]
                    end = i
            else:
                dp[i][j] = 0
                
    return s1[end - max_length: end]