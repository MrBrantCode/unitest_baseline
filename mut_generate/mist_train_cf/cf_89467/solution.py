"""
QUESTION:
Write a function `longest_common_substring` that takes two strings `s1` and `s2` as input and returns the length of the longest common substring between them. The function should handle case-insensitive strings, special characters, and multiple occurrences of the same substring within a string. The time complexity of the function should be O(n^2), where n is the length of the shorter string, and the space complexity should be O(n^2). The function should be implemented using dynamic programming.
"""

def longest_common_substring(s1, s2):
    # Convert the strings to lowercase 
    s1 = s1.lower()
    s2 = s2.lower()

    # Initialize a 2D matrix to store intermediate results
    dp = [[0] * (len(s2) + 1) for _ in range(len(s1) + 1)]

    # Initialize variables to store the length and ending index of the longest common substring
    max_length = 0

    # Calculate the length of the longest common substring using dynamic programming
    for i in range(1, len(s1) + 1):
        for j in range(1, len(s2) + 1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
                if dp[i][j] > max_length:
                    max_length = dp[i][j]

    # Return the length of the longest common substring
    return max_length