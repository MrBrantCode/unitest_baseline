"""
QUESTION:
Write a function `reverse_first_five` that takes a tuple as input, reverses the order of its first five elements, and returns them. If the tuple has fewer than five elements, include all of them in the reversed output.
"""

def reverse_first_five(input_tuple):
    return input_tuple[:5][::-1]