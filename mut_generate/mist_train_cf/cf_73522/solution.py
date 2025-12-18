"""
QUESTION:
Write a function `fizz(n)` and `buzz(n)` to print numbers from `n` to 100, where multiples of 3 are replaced by "Fizz", multiples of 5 are replaced by "Buzz", and multiples of both 3 and 5 are replaced by "FizzBuzz". The `fizz` function should call `buzz` and vice versa.
"""

def fizz(n):
    if n > 100:
        return
    if n % 3 == 0 and n % 5 == 0:
        print("FizzBuzz", end=" ")
    elif n % 3 == 0:
        print("Fizz", end=" ")
    else:
        buzz(n)

def buzz(n):
    if n % 5 == 0:
        print("Buzz", end=" ")
    else:
        print(n, end=" ")
    fizz(n+1)