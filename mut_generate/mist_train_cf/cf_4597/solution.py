"""
QUESTION:
Write a function `count_quadruples(nums)` that counts the number of quadruples in a given array `nums` of unique positive and negative numbers that sum up to zero. A quadruple is a set of four distinct numbers. The function should return the total count of such quadruples.
"""

def count_quadruples(nums):
    count = 0
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            for k in range(j+1, len(nums)):
                for l in range(k+1, len(nums)):
                    if nums[i] != nums[j] != nums[k] != nums[l]:
                        if nums[i] + nums[j] + nums[k] + nums[l] == 0:
                            count += 1
    return count