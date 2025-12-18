"""
QUESTION:
Write a function `get_positive_numbers` that takes a list of integers as input and returns a new list containing only the positive numbers. The function should have a time complexity of O(n) and the space complexity should be proportional to the number of positive numbers in the input list.
"""

def get_positive_numbers(nums):
    positive_nums = []
    
    for num in nums:
        if num > 0:
            positive_nums.append(num)
    
    return positive_nums