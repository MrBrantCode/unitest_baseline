"""
QUESTION:
Create a function called `pack_string` that takes an input string with a length between 8 and 20 characters, and returns an array of length 8 containing unique characters from the input string in their original order. The function should stop adding characters to the array once it reaches a length of 8.
"""

def pack_string(input_string):
    packed_array = []
    for char in input_string:
        if char not in packed_array and len(packed_array) < 8:
            packed_array.append(char)
        if len(packed_array) == 8:
            break
    return packed_array