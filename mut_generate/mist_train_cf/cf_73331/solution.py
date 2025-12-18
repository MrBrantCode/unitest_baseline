"""
QUESTION:
Create a function `maxMinProduct(nums)` that takes an array of integers `nums` as input and returns two values: the maximum value of `(nums[i]-1)*(nums[j]-1)` and the minimum value of `(nums[i]+1)*(nums[j]+1)`, where `i` and `j` are different indices of the array. The array has a length between 2 and 500, and each element is an integer between 1 and 10^3.
"""

def maxMinProduct(nums):
    max1, max2 = float('-inf'), float('-inf')
    min1, min2 = float('inf'), float('inf')

    for num in nums:
        if num > max1:
            max2 = max1
            max1 = num
        elif num > max2:
            max2 = num

        if num < min1:
            min2 = min1
            min1 = num
        elif num < min2:
            min2 = num

    return (max1-1) * (max2-1), (min1+1) * (min2+1)