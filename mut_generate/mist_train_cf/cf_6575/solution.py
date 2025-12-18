"""
QUESTION:
Create a function `fizz_buzz_dict` that generates a dictionary with keys from 1 to 100 and corresponding values based on the following conditions: numbers divisible by 3 should have the value "Fizz", numbers divisible by 5 should have the value "Buzz", and numbers divisible by both 3 and 5 should have the value "FizzBuzz", while other numbers have their string representation as values. The function should accept an optional "step" argument to determine the key increment, defaulting to 1, and implement this using a recursive approach without loops.
"""

def fizz_buzz_dict(n=1, step=1, result={}):
    """
    Generates a dictionary with keys from 1 to 100 and corresponding values based on the FizzBuzz rules.

    Args:
        n (int): The current key value. Defaults to 1.
        step (int): The key increment. Defaults to 1.
        result (dict): The dictionary to store the FizzBuzz values. Defaults to an empty dictionary.

    Returns:
        dict: The dictionary with FizzBuzz values.
    """
    if n > 100:
        return result

    if n % 3 == 0 and n % 5 == 0:
        result[n] = "FizzBuzz"
    elif n % 3 == 0:
        result[n] = "Fizz"
    elif n % 5 == 0:
        result[n] = "Buzz"
    else:
        result[n] = str(n)

    return fizz_buzz_dict(n + step, step, result)