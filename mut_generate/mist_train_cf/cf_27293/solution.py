"""
QUESTION:
Create a function `compress_string` that takes a string as input and returns its compressed version. The compression is done by replacing consecutive repeated characters with a single instance of the character followed by the number of repetitions. If the compressed string is not shorter than the original string, return the original string.
"""

def compress_string(s):
    compressed = ""
    count = 1
    for i in range(len(s)):
        if i < len(s) - 1 and s[i] == s[i + 1]:
            count += 1
        else:
            compressed += s[i] + str(count)
            count = 1
    return compressed if len(compressed) < len(s) else s