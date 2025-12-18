"""
QUESTION:
Write a function `string_compression(s)` that takes a string `s` as input and returns a string where consecutive duplicate characters are removed and the number of occurrences of each consecutive character is appended to the character. The function should have a time complexity of O(n), where n is the length of the string.
"""

def compress_string(s):
    result = ""
    i = 0

    while i < len(s):
        count = 1
        while i + 1 < len(s) and s[i] == s[i+1]:
            i += 1
            count += 1
        result += s[i] + str(count)
        i += 1
    return result