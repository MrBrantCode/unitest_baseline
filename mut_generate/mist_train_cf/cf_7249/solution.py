"""
QUESTION:
Create a function `longest_unique_substring(s)` that takes a string `s` as input, where `s` only contains lowercase English alphabets (a-z). The function should return the length of the longest substring with unique characters. If there are multiple substrings with the same longest length, the function should return the length of the lexicographically smallest substring.
"""

def longest_unique_substring(s):
    unique_chars = set()
    longest_length = 0
    longest_start = 0
    current_length = 0
    current_start = 0

    for i, char in enumerate(s):
        if char in unique_chars:
            if current_length > longest_length:
                longest_length = current_length
                longest_start = current_start

            current_length = 0
            current_start = i + 1
            unique_chars.clear()
        else:
            unique_chars.add(char)
            current_length += 1

    if current_length > longest_length:
        longest_length = current_length
        longest_start = current_start

    return longest_length