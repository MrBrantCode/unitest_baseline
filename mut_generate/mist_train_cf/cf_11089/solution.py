"""
QUESTION:
Write a function `remove_duplicates` that takes an array of integers as input and returns a list of all elements in the original array except for the duplicates. The function should have a time complexity of O(n), where n is the length of the array.
"""

def remove_duplicates(arr):
    seen = set()
    result = []
    
    for num in arr:
        if num not in seen:
            result.append(num)
            seen.add(num)
    
    return result