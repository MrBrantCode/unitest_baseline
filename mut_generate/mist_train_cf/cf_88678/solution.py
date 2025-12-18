"""
QUESTION:
Write a recursive function `sum_and_avg(arr)` that calculates the sum and average of all elements in a given array `arr` of integers using a divide-and-conquer algorithm. The function should return two values: the sum of all elements and their average. The array can be empty or contain one or more integers.
"""

def sum_and_avg(arr):
    if len(arr) == 0:
        return 0, 0
    elif len(arr) == 1:
        return arr[0], arr[0]
    else:
        mid = len(arr) // 2
        left_sum, left_avg = sum_and_avg(arr[:mid])
        right_sum, right_avg = sum_and_avg(arr[mid:])
        total_sum = left_sum + right_sum
        total_avg = (left_sum + right_sum) / len(arr)
        return total_sum, total_avg