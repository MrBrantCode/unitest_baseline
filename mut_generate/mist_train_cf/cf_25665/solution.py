"""
QUESTION:
Write a function `most_frequent_char(s)` that calculates the most frequent character in a given string `s`. The function should return the most frequent character. If there are multiple characters with the same highest frequency, the function should return any of them. The function should only consider the characters in the string and ignore any other factors. The input string `s` may contain any ASCII characters, including letters, numbers, and special characters.
"""

def most_frequent_char(s):
    counts = {}
    max_char = ""
    max_count = 0
    for c in s:
        if c in counts:
            counts[c] += 1
        else:
            counts[c] = 1
        if counts[c] > max_count:
            max_char = c
            max_count = counts[c]
    return max_char