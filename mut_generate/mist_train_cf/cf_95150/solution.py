"""
QUESTION:
Create a function named `format_numbers` that takes a list of numbers as input and returns a list of strings. Each string in the output list should represent a number from the input list, formatted with commas as thousands separators and rounded to the nearest hundredth decimal place. Exclude any numbers that are divisible by 5 from the final formatted list.
"""

def format_numbers(numbers):
    formatted_list = []
    for num in numbers:
        if num % 5 == 0:
            continue
        formatted_num = "{:,.2f}".format(round(num, 2))
        formatted_list.append(formatted_num)
    return formatted_list