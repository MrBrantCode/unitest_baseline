"""
QUESTION:
Write a function `sum_special` that takes an array of numbers as input and returns two values: the sum of all elements in the array and the sum of all elements at even indices in the array. The function must use a single loop to achieve this.
"""

def sum_special(arr):
    total_sum = 0
    sum_even_indices = 0
    for i in range(len(arr)):
        total_sum += arr[i]
        if i % 2 == 0:
            sum_even_indices += arr[i]
    return total_sum, sum_even_indices