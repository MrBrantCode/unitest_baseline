"""
QUESTION:
Write a function `get_array_size_in_bytes(array)` that takes an array of integers as input and returns the size of the array in bytes, assuming each integer is 8 bytes. The function should have a time complexity of O(1) and not use any built-in functions or libraries other than what's necessary to define the function and input array.
"""

def get_array_size_in_bytes(array):
    return len(array) * 8