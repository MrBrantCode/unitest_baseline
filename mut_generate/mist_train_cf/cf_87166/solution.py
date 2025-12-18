"""
QUESTION:
Implement a function `square(func, num)` that takes another function `func` and a number `num` as arguments, and returns the square of the result of `func(num)`. The function `func` should take a single number as an argument and return a result that can be squared. 

Restriction: The provided `func` may not actually square the input number, but may perform a different operation instead.
"""

def square(func, num):
    return func(num) ** 2