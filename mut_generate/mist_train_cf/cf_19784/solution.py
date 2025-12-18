"""
QUESTION:
Create a function called "fizzBuzz" that takes an integer as input and returns a string. The function should return "Fizz" if the number is divisible by 3, "Buzz" if the number is divisible by 5, and "FizzBuzz" if the number is divisible by both 3 and 5. The function should handle non-integer inputs and negative integers, returning "Invalid input" for non-integers. If the number is not divisible by either 3 or 5, the function should return "Not a multiple".
"""

def fizzBuzz(num):
    if type(num) != int:
        return "Invalid input"
    if num % 3 == 0 and num % 5 == 0:
        return "FizzBuzz"
    elif num % 3 == 0:
        return "Fizz"
    elif num % 5 == 0:
        return "Buzz"
    else:
        return "Not a multiple"