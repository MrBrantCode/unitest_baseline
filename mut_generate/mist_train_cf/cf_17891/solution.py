"""
QUESTION:
Write a recursive function `remove_even_duplicates(arr)` that takes an array of numbers as input, removes all even numbers and duplicates, and returns the resulting array. The function should have a time complexity of O(n^2) and handle arrays of any length containing both positive and negative numbers. If the input array is empty or only contains even numbers, the function should return an empty array.
"""

def remove_even_duplicates(arr):
    if not arr:
        return []
    first = arr[0]
    if first % 2 == 0:
        return remove_even_duplicates(arr[1:])
    return [first] + remove_even_duplicates([x for x in arr[1:] if x != first])