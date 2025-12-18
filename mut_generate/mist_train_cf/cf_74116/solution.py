"""
QUESTION:
Design a function `format_numbers` that takes a list of numbers as input and returns a list of strings where each number is formatted with a period as the decimal marker and a comma as the thousands separator. The function should handle both integer and floating-point numbers, rounding floating-point numbers to two decimal places. The input list only contains numbers.
"""

def format_numbers(numbers):
    formatted_numbers = []
    
    for number in numbers:
        # Check If The Number Is Float Or Not
        if isinstance(number, float):
            number = '{:,.2f}'.format(number)
            number = number.replace(".", "_")
            number = number.replace(",", ".")
            number = number.replace("_", ",")
        else:
            number = '{:,}'.format(number)
            number = number.replace(",", ".")
        
        formatted_numbers.append(number)
        
    return formatted_numbers