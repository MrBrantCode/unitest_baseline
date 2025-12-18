"""
QUESTION:
Implement the `stringCompressor` function, which takes a string `s` as input and returns the compressed version of the string. The function should replace consecutive repeated characters with the character followed by the count of consecutive occurrences. If the compressed string is not shorter than the original string, return the original string.
"""

def stringCompressor(s):
    compressed = ""
    count = 1
    for i in range(len(s)):
        if i + 1 < len(s) and s[i] == s[i + 1]:
            count += 1
        else:
            compressed += s[i] + str(count)
            count = 1
    return compressed if len(compressed) < len(s) else s