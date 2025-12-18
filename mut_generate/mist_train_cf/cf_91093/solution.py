"""
QUESTION:
Write a function `has_duplicate` that takes an array of integers as input and returns a boolean indicating whether the array contains any duplicate elements. The function must have a time complexity of O(n) and a space complexity of O(1), and it is guaranteed that the input array will only contain integers ranging from 1 to 1000.
"""

def has_duplicate(arr):
    unique_elements = set()
    for num in arr:
        if num in unique_elements:
            return True
        unique_elements.add(num)
    return False