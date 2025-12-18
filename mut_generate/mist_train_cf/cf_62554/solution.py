"""
QUESTION:
Compute the total Hamming distance between every possible pair of numbers in the given array. The Hamming distance is defined as the number of positions where the corresponding bits of two integers differ.

Given an array of integers where each element is within the range of 0 to 10^9 and the array's length does not exceed 10^4, write a function named `totalHammingDistance(nums)` to calculate the cumulative Hamming distance.
"""

def totalHammingDistance(nums):
    res = 0
    for i in range(32):
        currBit = sum(((num >> i) & 1) for num in nums)
        res += currBit * (len(nums) - currBit)
    return res