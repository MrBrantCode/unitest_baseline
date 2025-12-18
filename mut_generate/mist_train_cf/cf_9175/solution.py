"""
QUESTION:
Write a function named `calculate_average` that takes an array of numbers as input and returns the average of all non-negative numbers in the array. If the array does not contain any non-negative numbers, the function should return 0.
"""

def calculate_average(numbers):
    total_sum = 0
    count = 0
    
    for num in numbers:
        if num >= 0:
            total_sum += num
            count += 1
    
    return total_sum / count if count > 0 else 0