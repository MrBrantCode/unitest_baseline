"""
QUESTION:
Write a function called `remove_duplicates` that takes in a list of integers and returns a new list with duplicate elements removed, while maintaining the original order. The input list may contain both positive and negative integers, be empty, or contain only one element. Do not use any built-in Python functions or libraries, and do not modify the original list.
"""

def remove_duplicates(lst):
    result = []
    seen = set()
    
    for num in lst:
        if num not in seen:
            result.append(num)
            seen.add(num)
    
    return result