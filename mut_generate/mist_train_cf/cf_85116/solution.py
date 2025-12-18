"""
QUESTION:
Write a function `switch_chars(s)` that takes a string `s` as input and returns a new string where every character at an odd index is switched with the following character at an even index, while keeping the rest of the string unchanged.
"""

def switch_chars(s):
    output = list(s)
    for i in range(0, len(output)-1, 2):
        output[i], output[i+1] = output[i+1], output[i]
    return ''.join(output)