"""
QUESTION:
Create a recursive function called `all_digits_greater_than_five` that checks if every digit in a given positive integer is greater than 5. The function must not use any built-in function or method that converts integers to strings or arrays.
"""

def all_digits_greater_than_five(n):
    if n == 0:
        return True
    else:
        last_digit = n % 10
        return last_digit > 5 and all_digits_greater_than_five(n // 10)