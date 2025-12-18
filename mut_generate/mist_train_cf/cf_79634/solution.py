"""
QUESTION:
Write a function called `lengthiest_subsequence` that takes a string `s` as input and returns the length of the longest continuous subsequence within the string with no repeating characters.
"""

def lengthiest_subsequence(s):
    start = max_length = 0
    unique_chars = set()
    for i in range(len(s)):
        if s[i] not in unique_chars:
            unique_chars.add(s[i])
            max_length = max(max_length, len(unique_chars))
        else:
            while s[start] != s[i]:
                unique_chars.remove(s[start])
                start += 1
            start += 1
    return max_length