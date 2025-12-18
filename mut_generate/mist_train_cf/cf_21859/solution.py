"""
QUESTION:
Write a function `multiply_list_by_target_sum` that takes a list of integers and a target sum as input, and returns a new list where each element from the original list is multiplied by the absolute value of the target sum.
"""

def multiply_list_by_target_sum(lst, target_sum):
    return [num * abs(target_sum) for num in lst]