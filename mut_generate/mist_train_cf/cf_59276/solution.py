"""
QUESTION:
Write a function called `getMaxLen(nums)` that determines the maximum length of a subarray in the given array `nums` where the product of all its elements is positive.

The input array `nums` is an array of integers where `1 <= len(nums) <= 10^5` and `-10^9 <= nums[i] <= 10^9`. The function should return the maximum length of a subarray with a positive product.

Note: A subarray is a consecutive sequence of zero or more values extracted from the original array. If there is a 0 in the array, it should be excluded from the subarray as it would result in a product of 0, which is not positive.
"""

def getMaxLen(nums):
    n = len(nums)
    maxPositive = [0] * n
    maxNegative = [0] * n

    if nums[0] > 0:
        maxPositive[0] = 1
    elif nums[0] < 0:
        maxNegative[0] = 1
    
    for i in range(1, n):
        if nums[i] > 0:
            maxPositive[i] = maxPositive[i - 1] + 1
            maxNegative[i] = maxNegative[i - 1] + 1 if maxNegative[i - 1] > 0 else 0
        elif nums[i] < 0:
            maxPositive[i] = maxNegative[i - 1] + 1 if maxNegative[i - 1] > 0 else 0
            maxNegative[i] = maxPositive[i - 1] + 1
        else:
            maxPositive[i] = maxNegative[i] = 0

    return max(maxPositive)