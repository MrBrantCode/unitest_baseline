"""
QUESTION:
Write a function `compress_string` that takes a string of repeated characters as input and returns a compressed string where each repeated character is replaced by the character followed by the count of repetition. If the compressed string is not shorter than the original string, the function should return the original string.
"""

def compress_string(s: str) -> str:
    compressed = ''
    count = 1
    for i in range(len(s)):
        if i == len(s) - 1 or s[i] != s[i + 1]:
            compressed += s[i] + str(count)
            count = 1
        else:
            count += 1
    return compressed if len(compressed) < len(s) else s