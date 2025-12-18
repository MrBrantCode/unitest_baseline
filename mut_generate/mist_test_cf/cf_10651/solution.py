"""
QUESTION:
Write a function `check_duplicates` that takes an array of integers as input. The function should return `True` if the array contains any duplicate elements and `False` otherwise, given that the array is sorted in ascending order and its length is less than or equal to 100.
"""

def check_duplicates(arr):
    # Check if length of array exceeds 100
    if len(arr) > 100:
        return False
    
    # Check if array is sorted in ascending order
    if arr != sorted(arr):
        return False
    
    # Check if any duplicate elements exist
    seen = set()
    for num in arr:
        if num in seen:
            return True
        seen.add(num)
    
    return False