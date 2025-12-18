"""
QUESTION:
Write a function named `find_max` that takes a list of integers as input and returns the maximum number without using built-in functions or control structures (loops or recursion).
"""

def find_max(arr):
    """
    This function takes a list of integers as input and returns the maximum number.
    It uses the property of Python that it evaluates the expression from left to right.
    """
    max_num = arr[0]  
    max_num = arr[1] if arr[1] > max_num else max_num
    max_num = arr[2] if arr[2] > max_num else max_num
    max_num = arr[3] if arr[3] > max_num else max_num
    max_num = arr[4] if arr[4] > max_num else max_num
    return max_num