"""
QUESTION:
Create a function named `longest_common_substring` that takes two strings `s1` and `s2` and finds the longest common substring between them. The function should have a time complexity of O(n*m), where n is the length of `s1` and m is the length of `s2`. The function should return the longest common substring.
"""

def longest_common_substring(s1, s2):
    # Initialize a 2D array to store the lengths of longest common suffixes
    dp = [[0] * (len(s2) + 1) for _ in range(len(s1) + 1)]
    
    # Variable to store the length of the longest common substring
    max_len = 0
    
    # Variable to store the ending index of the longest common substring
    end_index = 0
    
    # Iterate over the characters of the first string
    for i in range(1, len(s1) + 1):
        # Iterate over the characters of the second string
        for j in range(1, len(s2) + 1):
            # If the characters match
            if s1[i - 1] == s2[j - 1]:
                # Update the length of longest common suffix
                dp[i][j] = dp[i - 1][j - 1] + 1
                # Check if the length is greater than the current maximum
                if dp[i][j] > max_len:
                    max_len = dp[i][j]
                    # Update the ending index of the longest common substring
                    end_index = i - 1
    
    # Extract the longest common substring from the first string
    longest_substring = s1[end_index - max_len + 1: end_index + 1]
    
    return longest_substring