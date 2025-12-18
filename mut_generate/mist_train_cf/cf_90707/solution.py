"""
QUESTION:
Create a function `square_and_hex_stringify` that takes a list of integers as input, squares each integer, converts the result to hexadecimal, and returns a string representation of the modified list, with each element separated by a comma and a space.
"""

def square_and_hex_stringify(lst):
    modified_lst = [hex(num**2)[2:] for num in lst]
    return ", ".join(modified_lst)