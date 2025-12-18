"""
QUESTION:
Create a function named `cube_sum` that takes an array of integers as input, replaces each element with its cube, and returns the rounded average of the cube numbers. The function should modify the input array in place.
"""

def cube_sum(arr):
    sum = 0
    for i in range(len(arr)):
        arr[i] = arr[i] ** 3
        sum += arr[i]
    average = round(sum / len(arr))
    return average