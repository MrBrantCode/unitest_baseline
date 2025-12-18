"""
QUESTION:
Write a function called `reverse_and_remove_duplicates` that takes a list of integers as input and returns a new list with the elements in reverse order, excluding duplicates and negative numbers. The function should have a time complexity of O(n), where n is the length of the input list.
"""

def reverse_and_remove_duplicates(nums):
    seen = set()
    result = []
    
    for num in reversed(nums):
        if num >= 0 and num not in seen:
            seen.add(num)
            result.append(num)
    
    return result