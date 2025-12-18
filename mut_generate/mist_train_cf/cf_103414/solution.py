"""
QUESTION:
Create a function named `validate_input` that checks if the given input is an integer between 2 and 6 (inclusive) and is divisible by 3. The function should return `True` if the input is valid and `False` otherwise. The function should handle cases where the input is not a valid integer.
"""

def validate_input(input_num):
    try:
        num = int(input_num)
        if num >= 2 and num <= 6 and num % 3 == 0:
            return True
        else:
            return False
    except ValueError:
        return False