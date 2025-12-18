"""
QUESTION:
Write a function called `calculate_average` that calculates the average of all elements in a given list of numbers. The function must have a time complexity of O(n) and use only a constant amount of extra space, handling both negative numbers and floating-point numbers.
"""

def calculate_average(lst):
    sum = 0
    count = 0

    for num in lst:
        sum += num
        count += 1

    average = sum / count
    return average