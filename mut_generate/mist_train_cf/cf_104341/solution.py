"""
QUESTION:
Write a function called `binary_list_to_int` that takes a list of binary digits as input and returns the integer value represented by the binary list. The binary list can contain up to 100 elements, and each element must be either 0 or 1. If the list is empty or contains invalid elements, the function should return 0 or None respectively.
"""

def binary_list_to_int(binary_list):
    if not binary_list:  
        return 0

    for bit in binary_list:
        if bit not in [0, 1]:  
            return None

    binary_string = "".join(str(bit) for bit in binary_list)
    return int(binary_string, 2)