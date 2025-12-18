"""
QUESTION:
Create a function `find_max_product` that takes a list of integers as input and returns the maximum product of each element and the sum of all elements in the list. The function must not use any built-in functions to calculate the sum of all elements in the list. The input list is guaranteed to be non-empty.
"""

def find_max_product(nums):
    def calculate_sum(index):
        if index == len(nums) - 1:
            return nums[index]
        return nums[index] + calculate_sum(index + 1)
    
    total_sum = calculate_sum(0)
    max_product = float('-inf')
    for i in range(len(nums)):
        product = nums[i] * total_sum
        max_product = max(max_product, product)
    return max_product