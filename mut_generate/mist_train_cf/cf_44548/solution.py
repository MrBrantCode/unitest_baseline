"""
QUESTION:
Write a function `compress_string(s)` that takes a string `s` as input and returns a new string where consecutive repeated characters are replaced with the character and the number of times it was repeated. If a character is not repeated, it remains unchanged. The function should preserve the original sequence of characters. The function should not use any external libraries or data structures other than built-in Python data types.
"""

def compress_string(s):
    result = ""
    counter = 1
    for i in range(len(s)):
        if i + 1 < len(s) and s[i] == s[i + 1]:
            counter += 1
        else:
            result += s[i] + (str(counter) if counter > 1 else "")
            counter = 1
    return result