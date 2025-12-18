"""
QUESTION:
Create a function named `sum_of_negatives` that uses recursion to calculate the sum of all negative numbers in a given array. The function should return 0 when the input array is empty.
"""

def sum_of_negatives(arr):
    if not arr:
        return 0
    else:
        current_num = arr[0]
        if current_num < 0:
            return current_num + sum_of_negatives(arr[1:])
        else:
            return sum_of_negatives(arr[1:])