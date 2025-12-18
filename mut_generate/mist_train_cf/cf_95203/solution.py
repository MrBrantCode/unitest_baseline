"""
QUESTION:
Write a function `remove_negatives_and_divisible_by_3(arr)` that takes an array of elements as input and returns a new array with all non-integer values, negative numbers, and numbers divisible by 3 removed. The output array should be sorted in descending order and contain no duplicates. If the input array is empty or does not contain any remaining numbers, return an empty array. The function should be optimized to have a time complexity of O(n) and be able to handle large input arrays efficiently.
"""

def remove_negatives_and_divisible_by_3(arr):
    result = set()
    for num in arr:
        if isinstance(num, int) and num % 1 == 0 and num >= 0 and num % 3 != 0:
            result.add(num)
    return sorted(list(result), reverse=True)