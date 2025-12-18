"""
QUESTION:
Create a function named `format_numbers` that takes a list of numbers as input. The function should round each number to the nearest hundredth decimal place and format it with commas as thousands separators. The function should return a list of strings, each representing a formatted number.
"""

def format_numbers(numbers):
    formatted_numbers = []
    
    for number in numbers:
        formatted_number = "{:,.2f}".format(round(number, 2))
        formatted_numbers.append(formatted_number)
    
    return formatted_numbers