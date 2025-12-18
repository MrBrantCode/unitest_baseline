"""
QUESTION:
Create a function called `find_sequence(input_string)` that takes a string `input_string` as input and returns the sequence of characters starting with 'a' and ending with 'b'. The function should be able to handle incorrect inputs and edge cases. If the input string does not contain 'a' or 'b', or if 'a' does not come before 'b', the function should return an error message.
"""

def find_sequence(input_string):
    if 'a' not in input_string or 'b' not in input_string:
        return "Input does not contain 'a' or 'b'"
    else:
        first_a = input_string.index('a')
        last_b = input_string.rindex('b')
        if first_a < last_b:
            return input_string[first_a:last_b+1]
        else:
            return "The sequence 'a' to 'b' does not form a valid sequence"