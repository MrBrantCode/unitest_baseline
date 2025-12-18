"""
QUESTION:
Write a function named removeDuplicates that takes an array of integers as input and returns a new array with duplicates removed. The integers in the array range from -10^5 to 10^5 and the array length does not exceed 10^4. The function should have a time complexity of O(n) and use only constant space.
"""

def removeDuplicates(nums):
    unique_set = set()
    result = []

    for num in nums:
        if num not in unique_set:
            unique_set.add(num)
            result.append(num)

    return result