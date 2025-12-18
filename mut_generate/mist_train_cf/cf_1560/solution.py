"""
QUESTION:
Write a function `find_average` that calculates the average of the numbers in the given array while also performing two additional operations: calculating the square of each number and incrementing the total sum by the number itself repeated 'num' times. The function should return the calculated average.

The function must take an array of integers as input and return the calculated average. The average should be calculated by summing all numbers in the array, including the additional increments, and then dividing by the length of the array.
"""

def find_average(arr, num):
    total_sum = 0
    length = len(arr)

    for i in arr:
        total_sum += i ** 2
        total_sum += i * num

    total_sum += sum(arr)
    return total_sum / length