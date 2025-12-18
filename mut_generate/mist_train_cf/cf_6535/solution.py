"""
QUESTION:
Write a function `longest_common_substring(s1, s2)` that takes two strings `s1` and `s2` as input and returns the length of the longest common substring between them. The function should be case-insensitive, handle special characters by considering 'é' and 'e' as equal characters, and use a 2D matrix to store intermediate results. The function should have a time complexity of O(n^2) and a space complexity of O(n^2), where n is the length of the shorter string.
"""

def longest_common_substring(s1, s2):
    # Convert the strings to lowercase and normalize special characters
    s1 = s1.lower()
    s2 = s2.lower()
    s1 = normalize_special_chars(s1)
    s2 = normalize_special_chars(s2)

    # Initialize a 2D matrix to store intermediate results
    dp = [[0] * (len(s2) + 1) for _ in range(len(s1) + 1)]

    # Initialize variables to store the length and ending index of the longest common substring
    max_length = 0
    end_index = 0

    # Calculate the length of the longest common substring using dynamic programming
    for i in range(1, len(s1) + 1):
        for j in range(1, len(s2) + 1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
                if dp[i][j] > max_length:
                    max_length = dp[i][j]
                    end_index = i

    # Return the length of the longest common substring
    return max_length

def normalize_special_chars(s):
    # Define a dictionary to normalize special characters
    special_chars = {'é': 'e', 'è': 'e', 'ê': 'e'}

    # Normalize special characters in the string
    normalized = ""
    for char in s:
        normalized += special_chars.get(char, char)

    return normalized