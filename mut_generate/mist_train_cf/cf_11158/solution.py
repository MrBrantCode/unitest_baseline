"""
QUESTION:
Implement a function named `verify_increasing` that takes an array of numbers as input and returns `True` if the array is in increasing order with all unique elements, and `False` otherwise. The array must contain at least 2 elements, may contain both positive and negative numbers, and may contain floating-point numbers. The function must have a time complexity of O(n) and cannot use built-in sorting functions or libraries.
"""

def verify_increasing(arr):
    if len(arr) < 2:
        return False
    
    seen = set()
    prev = arr[0]
    for num in arr:
        if num in seen or num <= prev:
            return False
        seen.add(num)
        prev = num
    
    return True