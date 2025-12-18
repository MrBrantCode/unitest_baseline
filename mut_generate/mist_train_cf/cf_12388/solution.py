"""
QUESTION:
Create a function called `check_fizz_buzz` that takes an integer as input and returns a string. The function should return "Fizz" if the number is divisible by 3, "Buzz" if it's divisible by 5, and "FizzBuzz" if it's divisible by both. If the input is not a valid integer, the function should return "Invalid input".
"""

def check_fizz_buzz(n):
    """
    Checks if a given number is divisible by 3, 5, or both.

    Args:
        n (int): The number to check.

    Returns:
        str: "Fizz" if the number is divisible by 3, "Buzz" if it's divisible by 5, 
             "FizzBuzz" if it's divisible by both, and "Invalid input" if the input is not a valid integer.
    """

    # Check if the input is a valid number
    if not isinstance(n, int):
        return "Invalid input"

    # Check if the number is divisible by both 3 and 5
    if n % 3 == 0 and n % 5 == 0:
        return "FizzBuzz"
    # Check if the number is divisible by 3
    elif n % 3 == 0:
        return "Fizz"
    # Check if the number is divisible by 5
    elif n % 5 == 0:
        return "Buzz"