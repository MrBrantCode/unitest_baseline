"""
QUESTION:
Write a function `countConsecutiveChars` that takes a string `s` of lowercase English letters as input and returns a list of tuples where each tuple contains a character and its consecutive count in the string. The function should return an empty list if the input string is empty.
"""

def count_consecutive_chars(s):
    if not s:
        return []

    result = []
    count = 1
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            result.append((s[i - 1], count))
            count = 1
    result.append((s[-1], count))
    return result