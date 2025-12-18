"""
QUESTION:
Write a function `findErrorNums(nums)` that takes an integer array `nums` representing a set of integers from 1 to n with a duplicate and a missing number. The function should return an array of two numbers, the duplicate and the missing number, without using any extra space (O(1) space complexity) and in O(n) time complexity. The input array `nums` contains integers in the range 1 to 10^4 and its length is between 2 and 10^4.
"""

def findErrorNums(nums):
    duplicate = -1
    n = len(nums)
    for i in range(n):
        num = abs(nums[i])
        if nums[num - 1] < 0:
            duplicate = num
        else:
            nums[num - 1] *= -1

    missing = -1
    for i in range(n):
        if nums[i] > 0:
            missing = i + 1
            break

    return [duplicate, missing]