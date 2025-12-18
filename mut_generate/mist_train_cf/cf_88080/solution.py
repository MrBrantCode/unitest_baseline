"""
QUESTION:
Create a function called `filter_and_sort` that takes an array of numbers as input and returns the first 5 unique numbers that are squares of numbers divisible by 3, sorted in descending order.
"""

def filter_and_sort(array):
    # Get the square of the numbers that are divisible by 3
    squares_divisible_by_3 = [num ** 2 for num in array if num % 3 == 0]
    
    # Get unique numbers and sort them in descending order
    unique_squares_divisible_by_3 = sorted(set(squares_divisible_by_3), reverse=True)
    
    return unique_squares_divisible_by_3[:5]