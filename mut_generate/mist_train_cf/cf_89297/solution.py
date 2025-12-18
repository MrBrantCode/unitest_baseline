"""
QUESTION:
Implement a function `find_max_product` that takes a list of integers `nums` as input and returns the maximum element in a new list. Each element in the new list is the product of its corresponding index in the original list and the sum of all elements in the original list. You must calculate the sum without using any loops or built-in functions like `sum()`. The list `nums` contains at least one element.
"""

def calculate_sum(nums, index):
    if index == len(nums) - 1:
        return nums[index]
    return nums[index] + calculate_sum(nums, index + 1)

def find_max_product(nums):
    total_sum = calculate_sum(nums, 0)
    return max(nums[i] * total_sum for i in range(len(nums)))