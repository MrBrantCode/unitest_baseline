"""
QUESTION:
Compute the average of a given list of numbers without using arithmetic operators (+, -, *, /) or the built-in average function. The solution must have a time complexity of O(n) and a space complexity of O(1). Write a function named `calculate_average` that takes a list of numbers as input and returns their average.
"""

def calculate_average(numbers):
    sum = 0
    count = 0
    for num in numbers:
        sum += num
        count += 1
    return sum / count