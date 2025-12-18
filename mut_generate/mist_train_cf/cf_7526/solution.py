"""
QUESTION:
Create a function `find_numbers_divisible_by_x_and_y(x, y, numbers)` that takes in three parameters: two integers `x` and `y`, and a list of integers `numbers`. The function should return a list of numbers from the `numbers` list that are divisible by both `x` and `y`. If no numbers meet this condition, return a message stating that there are no numbers divisible by both `x` and `y`. The function should also handle cases where `x` or `y` is not an integer or when `x` and `y` are equal to 0, returning an error message in such cases.
"""

def find_numbers_divisible_by_x_and_y(x, y, numbers):
    if not isinstance(x, int) or not isinstance(y, int):
        return "Error: x and y must be integers."
    elif x == 0 or y == 0:
        return "Error: x and y cannot be equal to 0."
    
    divisible_numbers = [num for num in numbers if num % x == 0 and num % y == 0]
    
    if not divisible_numbers:
        return f"There are no numbers divisible by both {x} and {y}."
    else:
        return divisible_numbers