"""
QUESTION:
Create a function `fizz_buzz` that prints the numbers from 1 to 100, replacing numbers divisible by 3 with "Fizz", numbers divisible by 5 with "Buzz", and numbers divisible by both 3 and 5 with "FizzBuzz". The function should use a custom `is_divisible` function to check for divisibility, which cannot use any mathematical operators or built-in functions for division or multiplication.
"""

def is_divisible(num, divisor):
    """Checks if a given number is divisible by a divisor without using division or multiplication."""
    while num >= divisor:
        num -= divisor
    return num == 0

def fizz_buzz():
    """Prints the numbers from 1 to 100, replacing numbers divisible by 3 with 'Fizz', numbers divisible by 5 with 'Buzz', and numbers divisible by both 3 and 5 with 'FizzBuzz'."""
    for i in range(1, 101):
        if is_divisible(i, 15):
            print("FizzBuzz")
        elif is_divisible(i, 3):
            print("Fizz")
        elif is_divisible(i, 5):
            print("Buzz")
        else:
            print(i)