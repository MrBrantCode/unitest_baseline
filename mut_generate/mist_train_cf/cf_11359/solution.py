"""
QUESTION:
Write a function `find_sum(arr, k)` that determines if two distinct elements from the array `arr` add up to a given number `k`. The array `arr` may contain negative numbers and duplicates, and the function should return `True` if such a pair exists and `False` otherwise.
"""

def find_sum(arr, k):
    unique_elements = set()
    
    for num in arr:
        if (k - num) in unique_elements:
            return True
        unique_elements.add(num)
    
    return False