"""
QUESTION:
Write a function `format_numbers(numbers, width)` that converts a list of numbers into a formatted string, handling negative numbers and maintaining the user-specified width constraint without introducing extra padding or cutting off digits.
"""

def format_numbers(numbers, width):
    # Define the format specifier for each number
    specifier = "{:>{}}"
    
    # Convert each number to a formatted string with sign and width
    formatted_numbers = [specifier.format(number, width) for number in numbers]
    
    # Join the formatted strings with a separator
    separator = ", "
    return separator.join(formatted_numbers)