"""
QUESTION:
Implement a function `calculate_mean` that takes a list of numbers as input and returns the mean of the numbers, rounded to 2 decimal places. The function must manually calculate the sum and count of the numbers using a loop, without using built-in functions like `sum()` and `len()`. The function should handle lists containing up to 1000 elements and floating-point numbers.
"""

def calculate_mean(numbers):
    total = 0
    count = 0
    for num in numbers:
        total += num
        count += 1
    
    mean = round(total / count, 2)
    return mean