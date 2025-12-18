"""
QUESTION:
Write a function `longest_non_repeating_substring(s)` that takes a string `s` as input and returns the longest consecutive substring of non-repeating characters in `s`. The function should return the longest substring in case of multiple substrings with the same maximum length. The input string `s` can contain any characters, including lowercase and uppercase letters, digits, and special characters. The function should be case sensitive and consider spaces and punctuation as characters.
"""

def longest_non_repeating_substring(s):
    max_len = 0
    start = 0
    seen = {}  # To store the last seen index of a character

    for end in range(len(s)):
        if s[end] in seen:
            # Update the start index if the character is already seen
            start = max(start, seen[s[end]] + 1)
        
        # Update the last seen index of the character
        seen[s[end]] = end

        # Update the maximum length
        max_len = max(max_len, end - start + 1)

    # Return the longest non-repeating substring
    return s[start:start+max_len]