"""
QUESTION:
Write a function named `binary_list_to_integer` that takes a list of binary digits as input and returns the corresponding integer value. The function should handle edge cases where the input list is empty or contains invalid elements (i.e., elements that are not 0 or 1). The time complexity of the function should be O(n), where n is the number of elements in the input list.
"""

def entrance(binary_list):
    if not binary_list or any(element not in [0, 1] for element in binary_list):
        return None
    
    decimal = 0
    for bit in binary_list:
        decimal = (decimal << 1) | bit
    
    return decimal