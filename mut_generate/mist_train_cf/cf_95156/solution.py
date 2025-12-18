"""
QUESTION:
Write a function named `cube_sum` that takes an array of integers as input. The function should replace each element of the array with its cube and then return the sum of all the cube numbers and the rounded average of these cube numbers.
"""

def cube_sum(arr):
    sum = 0
    for i in range(len(arr)):
        arr[i] = arr[i] ** 3
        sum += arr[i]
    average = round(sum / len(arr))
    return sum, average