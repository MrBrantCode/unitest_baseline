"""
QUESTION:
Implement a function named `lzw_compress` that compresses a given string using the LZW compression algorithm. The function should take one string parameter. The output should be a string where each character is followed by its count in the original string if the count is greater than 1, otherwise the count is omitted.
"""

def lzw_compress(s):
    compressed = ''
    count = 1
    for i in range(len(s)):
        if i < len(s) - 1 and s[i] == s[i+1]:
            count += 1
        else:
            compressed += s[i] + (str(count) if count > 1 else '')
            count = 1
    return compressed