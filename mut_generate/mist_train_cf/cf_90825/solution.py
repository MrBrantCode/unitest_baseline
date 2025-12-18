"""
QUESTION:
Design a function named `find_average` that calculates the average of an array of numbers. The function should be able to handle arrays containing both integers and floating-point numbers, return the average as a floating-point number with precision up to two decimal places, have a time complexity of O(n), and not use any built-in average calculation functions or libraries.
"""

def find_average(arr):
    total = 0
    count = 0

    for num in arr:
        total += num
        count += 1

    if count == 0:
        return 0

    average = total / count
    return round(average, 2)