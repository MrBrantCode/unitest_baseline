"""
QUESTION:
Create a function `format_numbers` that takes a list of numbers and returns a new list where each number is formatted with commas as thousands separators and rounded to the nearest hundredth decimal place, excluding any numbers that are divisible by 5.
"""

def format_numbers(numbers):
    formatted_list = []
    for num in numbers:
        if num % 5 == 0:
            continue
        formatted_num = "{:,.2f}".format(round(num, 2))
        formatted_list.append(formatted_num)
    return formatted_list