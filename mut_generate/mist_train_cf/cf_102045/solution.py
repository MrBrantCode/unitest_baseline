"""
QUESTION:
Write a function `has_duplicate(array)` that determines if an array contains duplicate elements. The array can contain integer elements ranging from 1 to 10^9, and the function should have a time complexity of O(n) and a space complexity of O(n).
"""

def has_duplicate(array):
    seen = set()
    for num in array:
        if num in seen:
            return True
        seen.add(num)
    return False