"""
QUESTION:
Write a function `binary_list_to_int` that takes a list of up to 100 binary digits (0 or 1) and returns the integer value represented by the binary list. The function should handle edge cases where the input list is empty or contains invalid elements, returning 0 and None respectively.
"""

def binary_list_to_int(binary_list):
    if not binary_list:  # If the binary list is empty
        return 0

    for bit in binary_list:
        if bit not in [0, 1]:  # If the binary list contains invalid elements
            return None

    binary_string = "".join(str(bit) for bit in binary_list)
    return int(binary_string, 2)