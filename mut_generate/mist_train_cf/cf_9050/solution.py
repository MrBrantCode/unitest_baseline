"""
QUESTION:
Create a function named `square_and_hex_stringify` that takes a list of integers as input. The function should square each integer, convert it to hexadecimal, remove the '0x' prefix, and return a string representation of the modified list with each value separated by a comma and a space.
"""

def square_and_hex_stringify(lst):
    modified_lst = [hex(num**2)[2:] for num in lst]
    return ", ".join(modified_lst)