"""
QUESTION:
Write a function named `minMoves2` that takes a list of integers as input and returns the minimum number of moves required to make all elements at even indices equal to the median of the elements at even indices. A move is either incrementing or decrementing an element at an even index by 1. The length of the list is between 2 and 10,000 (inclusive), and the integers in the list are in the range of -10^6 to 10^6. If it's not possible to make all elements equal under these constraints, return -1.
"""

def minMoves2(nums):
    nums = sorted(nums[::2])
    median = nums[len(nums) // 2]

    return sum(abs(num - median) for num in nums)