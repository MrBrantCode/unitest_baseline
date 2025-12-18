"""
QUESTION:
Design a function `remove_duplicates` that takes an unsorted array of integers as input, removes all duplicates in-place while maintaining their relative order, and returns the resulting array. The function should have a time complexity of O(n), where n is the number of elements in the array, and handle negative numbers and zero.
"""

def remove_duplicates(nums):
    if len(nums) < 2:
        return nums

    # Use a dictionary to keep track of seen values
    seen = {}
    result = []
    for num in nums:
        if num not in seen:
            seen[num] = True
            result.append(num)

    return result