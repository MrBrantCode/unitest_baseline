"""
QUESTION:
Write a function named `extract_integer` that takes one input parameter `number`. The function should return the largest integer less than or equal to the given number. 

Restrictions and error handling: 

- If the input is not a float or an integer, return 'Error: Invalid input.'
- If the input is a very large number (greater than 1.7e308), return 'Error: Number too large.'
- The function should work for both positive and negative numbers.
- For zero input, return zero.
"""

def extract_integer(number):
    try:
        if not isinstance(number, (float, int)):
            return 'Error: Invalid input.'
        if abs(number) > 1.7e308:
            return 'Error: Number too large.'
        return int(number // 1) if number >= 0 else int(number // 1) - 1
    except TypeError:
        return 'Error: Invalid input.'
    except OverflowError:
        return 'Error: Number too large.'