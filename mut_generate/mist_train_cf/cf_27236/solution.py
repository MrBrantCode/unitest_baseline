"""
QUESTION:
Write a function called `calculate_average` that takes a list of numbers as input and returns the average of those numbers without using any built-in Python functions or libraries for mathematical operations. The function should handle an empty input list and avoid division by zero.
"""

def calculate_average(numbers):
    total = 0
    count = 0
    for num in numbers:
        total += num
        count += 1
    if count == 0:
        return 0  
    return total / float(count)