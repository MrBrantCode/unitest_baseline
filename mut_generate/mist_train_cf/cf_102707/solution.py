"""
QUESTION:
Write a function called `find_duplicates` that takes an array of integers as input, finds all duplicate elements in the array, and returns them in ascending order. The function should only return each duplicate element once, even if it appears more than twice in the array.
"""

def find_duplicates(arr):
    seen = set()
    duplicates = []
    
    for num in arr:
        if num in seen and num not in duplicates:
            duplicates.append(num)
        seen.add(num)
    
    duplicates.sort()
    return duplicates