"""
QUESTION:
Implement a function `verify_increasing` that checks whether an array of numbers is in increasing order with all unique elements. The function should have a time complexity of O(n), where n is the number of elements in the array. The array must contain at least 2 elements and can have both positive and negative numbers, including floating-point numbers. The function should return `True` if the array is in increasing order with unique elements and `False` otherwise.
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