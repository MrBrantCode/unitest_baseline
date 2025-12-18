"""
QUESTION:
Create a function `reverse_string(s)` that takes a string `s` as input and reverses the order of alphanumeric characters in-place, excluding special characters, and returns the modified string. The function should handle strings of any length, including empty strings and strings with only one character.
"""

def reverse_string(s):
    i, j = 0, len(s) - 1

    if len(s) == 0 or len(s) == 1:
        return s

    s = list(s)

    while i < j:
        if not s[i].isalnum():
            i += 1
        elif not s[j].isalnum():
            j -= 1
        else:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1

    s = ''.join(s)

    return s