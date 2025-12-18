"""
QUESTION:
Write a function named `result` that takes an integer `number` as input and returns a string based on its divisibility by 3, 5, and 7. The function should return "FizzBuzzBoom" if divisible by all three, "FizzBoom" if divisible by 3 and 7, "BuzzBoom" if divisible by 5 and 7, "Fizz" if divisible by 3, "Buzz" if divisible by 5, "Boom" if divisible by 7, and the input number itself otherwise.
"""

def result(number):
    """
    This function takes an integer as input and returns a string based on its divisibility by 3, 5, and 7.

    Parameters:
    number (int): The input number to check for divisibility.

    Returns:
    str: A string indicating the divisibility of the input number.
    """
    return "FizzBuzzBoom" if number % 3 == 0 and number % 5 == 0 and number % 7 == 0 else \
           "FizzBoom" if number % 3 == 0 and number % 7 == 0 else \
           "BuzzBoom" if number % 5 == 0 and number % 7 == 0 else \
           "Fizz" if number % 3 == 0 else \
           "Buzz" if number % 5 == 0 else \
           "Boom" if number % 7 == 0 else \
           str(number)