"""
QUESTION:
Create a function named `format_number` that takes a single number as input. The function should format the number with exactly five decimal places (rounding down), use spaces as thousands separators, and return the formatted string. However, the function should only accept numbers that are divisible by 7 and return "Invalid input! The number should be divisible by 7." for any other numbers.
"""

def format_number(num):
    if num % 7 == 0:
        formatted_num = '{:,.5f}'.format(num).replace(',', ' ')
        return formatted_num[:-1] if formatted_num[-1] == '0' else formatted_num
    else:
        return "Invalid input! The number should be divisible by 7."