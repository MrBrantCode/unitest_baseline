"""
QUESTION:
Write a function `sum_and_avg` that calculates the sum and average of an array of integers using a divide-and-conquer algorithm. The function should take an array of integers as input, and return a tuple containing the sum and average of the elements in the array. The function should be implemented recursively, and the array should be divided in half at each level of recursion.
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