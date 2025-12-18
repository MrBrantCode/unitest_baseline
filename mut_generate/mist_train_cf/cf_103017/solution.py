"""
QUESTION:
Write a function named `binary_to_integer` that takes a list of up to 20 binary digits (0 or 1) and returns the corresponding integer value. The function should handle edge cases where the input list is empty or contains invalid elements, returning 0 in such cases.
"""

def binary_to_integer(binary_list):
    # Check if the binary list is empty
    if not binary_list:
        return 0

    # Check if the binary list contains invalid elements
    if not all(bit == 0 or bit == 1 for bit in binary_list):
        return 0

    # Convert the binary list to a string
    binary_string = ''.join(str(bit) for bit in binary_list)

    # Convert the binary string to an integer
    integer_value = int(binary_string, 2)

    return integer_value