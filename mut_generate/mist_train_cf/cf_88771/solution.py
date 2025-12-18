"""
QUESTION:
Create a function called "fizzBuzz" that takes an integer as an argument. The function should return "Fizz" if the number is divisible by 3, "Buzz" if the number is divisible by 5, and "FizzBuzz" if the number is divisible by both 3 and 5. If the input is not an integer, the function should return "Invalid input". If the number is not divisible by either 3 or 5, the function should return "Not a multiple". The function should have a time complexity of O(1) and should not use any built-in functions or mathematical operators to determine divisibility, except for the modulo operator.
"""

def fizzBuzz(num):
    if not isinstance(num, int):
        return "Invalid input"
    
    if num % 3 == 0 and num % 5 == 0:
        return "FizzBuzz"
    
    if num % 3 == 0:
        return "Fizz"
    
    if num % 5 == 0:
        return "Buzz"
    
    return "Not a multiple"