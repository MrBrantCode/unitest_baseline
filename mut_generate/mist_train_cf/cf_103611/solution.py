"""
QUESTION:
Write a function called `fizz_buzz` that takes one integer parameter `n` representing the end number. The function should generate a list of numbers and strings from 1 to `n` (inclusive), where multiples of 3 are replaced with "Fizz", multiples of 5 are replaced with "Buzz", and multiples of both 3 and 5 are replaced with "FizzBuzz".
"""

def fizz_buzz(n):
    """
    Generate a list of numbers and strings from 1 to n (inclusive), 
    where multiples of 3 are replaced with "Fizz", multiples of 5 are replaced with "Buzz", 
    and multiples of both 3 and 5 are replaced with "FizzBuzz".

    Args:
    n (int): The end number.

    Returns:
    list: A list of numbers and strings.
    """
    result = []
    for num in range(1, n + 1):
        if num % 3 == 0 and num % 5 == 0:
            result.append("FizzBuzz")
        elif num % 3 == 0:
            result.append("Fizz")
        elif num % 5 == 0:
            result.append("Buzz")
        else:
            result.append(num)
    return result