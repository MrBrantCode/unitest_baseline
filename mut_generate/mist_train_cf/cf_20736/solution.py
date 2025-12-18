"""
QUESTION:
Write a function named `two_sum` that takes two inputs: an array of positive integers (`nums`) and a target sum (`target`). The function should return the indices of two numbers in the array that add up to the target sum. If no such pair exists, return an empty array. The solution must have a time complexity of O(n), where n is the length of the array.
"""

def two_sum(nums, target):
    hash_table = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in hash_table:
            return [hash_table[complement], i]
        hash_table[num] = i
    return []