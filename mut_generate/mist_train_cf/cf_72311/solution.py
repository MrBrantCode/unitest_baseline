"""
QUESTION:
Implement a function called "convert_to_string" that takes a list of integers as input and returns the list as a string, converting the integers to their respective characters (based on ASCII values) and applying a Caesar cipher to each character with a given shift value.

The function should have two parameters: 
- input_list: a list of integers (length between 1 and 100, each integer between 0 and 127)
- shift: an integer representing the number of characters to shift each character by (could be positive, negative, or zero)

The function should handle wrap-around if the ASCII value goes below 0 or above 127 after applying the shift.
"""

def convert_to_string(input_list, shift):
    def caesar_cipher(char, shift):
        ascii_val = (char + shift) % 128
        if ascii_val < 0:
            ascii_val += 128
        return chr(ascii_val)
    return ''.join(caesar_cipher(i, shift) for i in input_list)