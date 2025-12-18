"""
QUESTION:
Create a function called `create_new_array` that takes a list of integers as input. This function should create a new list containing only the positive integers from the input list, sorted in ascending order, with no duplicates. Additionally, the function should calculate the sum of the positive integers in the resulting list. The time complexity of the function should be O(n log n) or better.
"""

def create_new_array(arr):
    result = []
    for num in arr:
        if num > 0:
            result.append(num)
    result = sorted(set(result))
    positive_sum = sum(result)
    return result, positive_sum