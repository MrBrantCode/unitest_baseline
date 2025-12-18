"""
QUESTION:
Write a function `find_cube_triplets` that takes a list of positive integers as input and returns the cumulative count of non-overlapping adjacent triplets where the product of the three numbers is a perfect cube. The function should not consider overlapping triplets.
"""

def find_cube_triplets(nums):
    count = 0
    for i in range(len(nums) - 2):
        product = nums[i] * nums[i + 1] * nums[i + 2]
        if round(product ** (1/3)) ** 3 == product:
            count += 1
    return count