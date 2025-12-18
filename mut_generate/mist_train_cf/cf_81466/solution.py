"""
QUESTION:
Implement a function `eliminate_repeats(nums)` that takes a list of integers `nums` as input, removes duplicates while preserving the original order, and returns the filtered list. The function should run in a time complexity of O(n) and handle lists of arbitrary size. The output should only include the first occurrence of each integer.
"""

def eliminate_repeats(nums):
    seen = {}
    output = []
    for num in nums:
        if num not in seen:
            seen[num] = True
            output.append(num)
    return output