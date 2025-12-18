"""
QUESTION:
Implement a function called `compress_string` that compresses a given string by counting the occurrences of each character and returns the compressed string in the format "count-character". The function should consider non-contiguous blocks of the same character. The input string only contains uppercase letters.
"""

def compress_string(s):
    result = ""
    i = 0

    while i < len(s):
        count = 1
        while i + 1 < len(s) and s[i] == s[i + 1]:
            i += 1
            count += 1
        result += str(count) + s[i]
        i += 1

    return result