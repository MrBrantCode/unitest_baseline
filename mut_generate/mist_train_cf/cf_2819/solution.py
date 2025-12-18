"""
QUESTION:
Write a function named `binary_list_to_integer` that takes a binary list as input, which can contain up to 100 elements with values of either 0 or 1. The function should return the integer value of the binary list. If the binary list is empty or contains any invalid elements, the function should return None. The function should have a time complexity of O(n), where n is the number of elements in the binary list. The binary list is in little-endian format, where the least significant bit is at index 0.
"""

def binary_list_to_integer(binary_list):
    if not binary_list or any(element not in [0, 1] for element in binary_list):
        return None
    
    decimal = 0
    for bit in binary_list:
        decimal = (decimal << 1) | bit
    
    return decimal