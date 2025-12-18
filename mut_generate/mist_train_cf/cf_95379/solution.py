"""
QUESTION:
Implement the function `compress_string(s)` that takes a non-empty string `s` of lowercase alphabets and returns the compressed string using the Run-Length Encoding (RLE) algorithm. The function should achieve a time complexity of O(n), where n is the length of the input string `s`.
"""

def compress_string(s):
    if len(s) == 0:
        return ""

    result = ""
    current_char = s[0]
    count = 1

    for i in range(1, len(s)):
        if s[i] == current_char:
            count += 1
        else:
            result += current_char + str(count)
            current_char = s[i]
            count = 1

    result += current_char + str(count)

    return result