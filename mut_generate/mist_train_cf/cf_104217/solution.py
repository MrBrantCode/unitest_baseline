"""
QUESTION:
Given an array of integers where each integer is stored as 4 bytes, write a function `array_size_in_bytes` that calculates and returns the size of the array in bytes. The function should have a time complexity of O(1) and should not use any built-in functions or libraries.
"""

def array_size_in_bytes(array_size):
    """
    Calculates the size of an array of integers stored as 4 bytes in bytes.
    
    Args:
        array_size (int): The size of the array.
    
    Returns:
        int: The size of the array in bytes.
    """
    return array_size * 4