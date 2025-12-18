"""
QUESTION:
Write a function `calculate_median` that takes a string of comma-separated numbers as input, calculates the median of the list, and returns the result. The function should be able to handle both positive and negative integers, as well as decimal numbers, and should be able to handle lists with duplicate numbers. The function should not create any visual output; it should only return the calculated median.
"""

def calculate_median(numbers_str):
    numbers = [float(num) for num in numbers_str.split(',')]
    numbers.sort()
    n = len(numbers)
    
    if n % 2 == 0:
        median = (numbers[n//2 - 1] + numbers[n//2]) / 2
    else:
        median = numbers[n//2]
    
    return median