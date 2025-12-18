"""
QUESTION:
Write a function `second_minimum_index(nums)` that takes a list of numbers as input and returns the index of the second smallest element in the list. The function should iterate through the list only once.
"""

def second_minimum_index(nums):
    min_num = float('inf')
    second_min_num = float('inf')
    min_index = -1
    second_min_index = -1

    for i, num in enumerate(nums):
        if num < min_num:
            second_min_num = min_num
            second_min_index = min_index
            min_num = num
            min_index = i
        elif num < second_min_num:
            second_min_num = num
            second_min_index = i
    
    return second_min_index