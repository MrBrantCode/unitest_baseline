"""
QUESTION:
Write a function `remove_even_duplicates` that takes an array of integers as input, removes all even numbers and duplicates, and returns the resulting array. If the input array is empty or only contains even numbers, return an empty array. The order of numbers in the output array does not matter. The input array can contain both positive and negative numbers and can be of any length.
"""

def remove_even_duplicates(arr):
    # Check if the array is empty or contains only even numbers
    if not arr or all(num % 2 == 0 for num in arr):
        return []

    # Remove even numbers and duplicates from the array
    result = []
    seen = set()
    for num in arr:
        if num % 2 != 0 and num not in seen:
            result.append(num)
            seen.add(num)

    return result