"""
QUESTION:
Design a function named `remove_punctuation` that takes two parameters: `input_string` and `punctuation`. The function should remove all occurrences of the specified `punctuation` from the `input_string` while preserving the positions of other punctuation marks and characters. The function should return the modified string.
"""

def remove_punctuation(input_string, punctuation):
    output_string = ""
    for char in input_string:
        if char not in punctuation:
            output_string += char
    return output_string