"""
QUESTION:
Write a function `calculate_sum` that takes an array of up to 1000 elements as input, converts each element to a floating-point number, and returns the sum of all numbers in the array. The function should handle negative numbers and floating-point numbers, and it should return an error message if the input array contains non-numeric values.
"""

def calculate_sum(numbers):
    try:
        total_sum = 0
        for number in numbers:
            total_sum += float(number)  # Convert the number to float
        return total_sum
    except (TypeError, ValueError):
        return "Invalid input! Please provide a valid list of numbers."