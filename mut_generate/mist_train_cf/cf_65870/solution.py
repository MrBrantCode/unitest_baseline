"""
QUESTION:
Given a function name `pluck`, create a function that takes an array of non-negative integers and a condition function `cond_fn` as input. The function should return the smallest node value that fulfills the condition set by `cond_fn` along with its index in the array. If multiple nodes fulfill the condition with the smallest value, return the one with the smallest index. If the array is empty or no values meet the condition, return an empty list. The return format should be `[smallest_value, its_index]`. The `cond_fn` takes an integer as input and returns a boolean. The array length is between 1 and 1,000,000.
"""

def pluck(arr, cond_fn):
    result = []
    smallest_num = float('inf')
    smallest_index = float('inf')
    for i, num in enumerate(arr):
        if cond_fn(num) and num < smallest_num:
            smallest_num = num
            smallest_index = i
        elif cond_fn(num) and num == smallest_num and i < smallest_index:
            smallest_index = i
    if smallest_num != float('inf'):
        result.append(smallest_num)
        result.append(smallest_index)
    return result