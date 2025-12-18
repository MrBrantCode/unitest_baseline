"""
QUESTION:
Write a function `calculate_sum` that calculates the sum of all numbers in a given list. The function should handle both negative numbers and floating-point numbers, and it should be able to handle lists containing up to 1000 elements. If the input is not a list or contains non-numeric values, the function should return an error message.
"""

def calculate_sum(numbers):
    try:
        total_sum = 0
        for number in numbers:
            total_sum += float(number)  
        return total_sum
    except (TypeError, ValueError):
        return "Invalid input! Please provide a valid list of numbers."