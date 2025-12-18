"""
QUESTION:
Create a function called "fizzBuzz" that takes an integer as input and returns a string. The function should return "Fizz" if the number is divisible by 3, "Buzz" if the number is divisible by 5, "FizzBuzz" if the number is divisible by both 3 and 5, and "Not a multiple" if the number is not divisible by either 3 or 5. The function should return "Invalid input" if the input is not an integer. The function should have a time complexity of O(1).
"""

def fizzBuzz(num):
    # Check if the input is an integer
    if not isinstance(num, int):
        return "Invalid input"

    # Check if the number is divisible by both 3 and 5
    if num % 3 == 0 and num % 5 == 0:
        return "FizzBuzz"

    # Check if the number is divisible by 3
    if num % 3 == 0:
        return "Fizz"

    # Check if the number is divisible by 5
    if num % 5 == 0:
        return "Buzz"

    # If the number is not divisible by either 3 or 5
    return "Not a multiple"