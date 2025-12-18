"""
QUESTION:
Write a function named `sum_every_third_element` that calculates the sum of every third element in an array with a specific skipping pattern. The pattern starts by skipping 2 elements, then 3 elements, then 4 elements, and so on, until the end of the array is reached. The function should take an array as input and return the calculated sum. The array index starts at 0.
"""

def sum_every_third_element(arr):
    skip = 2
    total_sum = 0
    index = 0

    while index < len(arr):
        total_sum += arr[index]
        index += skip + 1
        skip += 1

    return total_sum