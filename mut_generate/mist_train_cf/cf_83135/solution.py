"""
QUESTION:
Create a function `cumulative_sum` that takes an array of numerical integers as input and returns a new array where each element at each index is the sum of all elements up to that index in the original array.
"""

def cumulative_sum(array):
    total = 0
    cumulative_sum_list = []
    for num in array:
        total += num
        cumulative_sum_list.append(total)
    return cumulative_sum_list