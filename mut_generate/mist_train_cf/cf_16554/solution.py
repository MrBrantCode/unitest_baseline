"""
QUESTION:
Create a function named `sum_except_index` that takes an array of positive integers as input and returns a new array. In the output array, each element at a given index should be the sum of all the numbers in the input array except for the number at the corresponding index. The input array will only contain positive integers and will not contain any zeros or negative numbers.
"""

def sum_except_index(lst):
    total_sum = sum(lst)
    return [total_sum - num for num in lst]