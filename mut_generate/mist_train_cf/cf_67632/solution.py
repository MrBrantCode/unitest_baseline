"""
QUESTION:
Create a function `run_length_encoding` that compresses an input string using the Run-length encoding algorithm. The function should return a string where sequences of the same character are represented as the character followed by the number of times it appears in the sequence.
"""

def run_length_encoding(input_string):
    if not input_string:
        return ''

    result = ''
    current_char = input_string[0]
    count = 1

    for char in input_string[1:]:
        if char == current_char:
            count += 1
        else:
            result += current_char + str(count)
            current_char = char
            count = 1

    result += current_char + str(count)
    return result