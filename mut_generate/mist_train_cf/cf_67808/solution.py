"""
QUESTION:
Write a function `interchange_characters(s)` that takes a string `s` as input. The function should interchange each odd-positioned character in the string with the subsequent even-positioned character, keeping all other characters in their original position. The input string `s` consists only of alphabetic characters and its length is at least 2. The function should return the modified string.
"""

def interchange_characters(s):
    new_s = list(s)

    for i in range(0, len(new_s) - 1, 2):
        new_s[i], new_s[i + 1] = new_s[i + 1], new_s[i]
    
    return "".join(new_s)