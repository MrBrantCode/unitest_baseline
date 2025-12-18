"""
QUESTION:
Implement a function called `remove_duplicates` that takes a list of integers as input and returns the list with duplicate elements removed while preserving the original order of the remaining elements. The function should have a time complexity of O(n) and a space complexity of O(n) in the worst case, where n is the number of elements in the input list.
"""

def remove_duplicates(arr):
    seen = set()
    result = []
    for num in arr:
        if num not in seen:
            result.append(num)
            seen.add(num)
    return result