"""
QUESTION:
Design a function named `remove_duplicates` that takes an array of integers as input and returns the array with all duplicates removed, maintaining the relative order of the remaining elements. The function should have a time complexity of O(n), where n is the number of elements in the array, and handle negative numbers and zero. The function should remove all occurrences of duplicates, not just one occurrence, and return the modified array.
"""

def remove_duplicates(arr):
    if len(arr) < 2:
        return arr

    seen = {}
    result = []
    for num in arr:
        if num not in seen:
            seen[num] = True
            result.append(num)

    return result