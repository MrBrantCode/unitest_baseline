"""
QUESTION:
Create a function called `longest_non_repeating_substring(s)` that takes a string `s` as input and returns the longest consecutive string of non-repeating characters in `s`. The function should return the first longest non-repeating substring it encounters in case of a tie.
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