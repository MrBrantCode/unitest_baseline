"""
QUESTION:
Create a function called `check_divisibility` that takes a numerical value as input. The function should return True if the input is evenly divisible by both 5 and 8. The function should handle inputs in both integer and string format. If the input string cannot be converted to a number, the function should return False. The function should be optimized to work with large numerical values.
"""

def entrance(x):
    try:
        n = int(x) if isinstance(x, str) else x
    except ValueError:
        return False
    return n % 5 == 0 and n % 8 == 0