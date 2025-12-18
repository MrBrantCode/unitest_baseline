"""
QUESTION:
Design a function called `find_average` that calculates the average of an array of numbers, which can be either integers or floating-point numbers. The function should return the average as a floating-point number with precision up to two decimal places, and it should have a time complexity of O(n), where n is the length of the input array. The function should not use any built-in average calculation functions or libraries.
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