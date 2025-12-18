"""
QUESTION:
Implement a function `string_compressor` that takes a string `s` as input and returns its compressed version. The compressed string consists of repeated characters followed by the count of consecutive occurrences. The function should return the original string if the compressed string is not shorter. The input string contains only uppercase and lowercase letters and can have a maximum length of 10^9 characters. The function should be case-insensitive and minimize time and space complexity.
"""

def string_compressor(s):
    compressed = ""
    count = 1
    for i in range(1, len(s)):
        if s[i].lower() == s[i-1].lower():
            count += 1
        else:
            compressed += s[i-1] + str(count)
            count = 1
    compressed += s[-1] + str(count)
    if len(compressed) >= len(s):
        return s
    else:
        return compressed