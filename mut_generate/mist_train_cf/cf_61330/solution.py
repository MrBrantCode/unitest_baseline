"""
QUESTION:
### is_integers_in_sum

Given an array of integers, write a function `is_integers_in_sum` that takes two integers `target_sum` and `previous_sum` as parameters, and returns a boolean value. The function should check if there are two numbers in the array that add up to `target_sum` when the array has not been traversed, and `previous_sum` when the array has been traversed.
"""

def is_integers_in_sum(arr, target_sum, previous_sum):
    if not arr:
        return False

    arr_set = set()
    for num in arr:
        if previous_sum - num in arr_set or target_sum - num in arr_set:
            return True
        arr_set.add(num)
    return False