"""
QUESTION:
Create a function named `interchange` that takes a string as input and returns a new string. The function should swap each character at an odd position (1-indexed) with the character two positions ahead of it, while leaving characters at even positions and non-alphabetic characters unchanged.
"""

def interchange(input_string):
    input_list = list(input_string)
    length = len(input_list)

    for i in range(0, length, 4):    # iterating over odd-positions
        if i + 2 < length:
            input_list[i], input_list[i+2] = input_list[i+2], input_list[i]    # swapping the characters

    return ''.join(input_list)