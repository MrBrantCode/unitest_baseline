"""
QUESTION:
Create a function `remove_negatives_and_divisible_by_3(arr)` that takes an array of integers as input, removes all negative numbers and numbers that are divisible by 3, and returns the remaining numbers in a sorted descending order with no duplicates. The function should ignore non-numeric and non-integer values in the input array.
"""

def remove_negatives_and_divisible_by_3(arr):
    result = []
    seen = set()
    for num in arr:
        if isinstance(num, int) and num % 1 == 0 and num >= 0 and num % 3 != 0 and num not in seen:
            result.append(num)
            seen.add(num)
    result.sort(reverse=True)
    return result