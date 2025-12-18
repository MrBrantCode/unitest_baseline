"""
QUESTION:
Create a function `transform_list_to_dict(nums)` that takes a list of integers as input. The function should return a dictionary where the keys are numbers from the input list that are divisible by 3, and the corresponding values are the cubes of these numbers. The input list should not contain any duplicates, and the numbers in the dictionary should be in descending order.
"""

def transform_list_to_dict(nums):
    unique_nums = sorted(list(set(nums)), reverse=True)
    
    result = {}
    for num in unique_nums:
        if num % 3 == 0:
            result[num] = num ** 3
        
    return result