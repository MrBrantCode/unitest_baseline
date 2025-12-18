"""
QUESTION:
Create a FizzBuzz function that prints numbers from 1 to 100, replacing multiples of 3 with "Fizz", multiples of 5 with "Buzz", and multiples of both with "FizzBuzz". Implement a custom function to check for divisibility using only bitwise operators, without using mathematical operators or built-in functions like division or multiplication.
"""

def FizzBuzz(n):
    def is_divisible(numerator, divisor):
        while numerator >= divisor:
            numerator -= divisor
        return numerator == 0

    for i in range(1, n+1):
        if is_divisible(i, 15):
            print("FizzBuzz")
        elif is_divisible(i, 3):
            print("Fizz")
        elif is_divisible(i, 5):
            print("Buzz")
        else:
            print(i)