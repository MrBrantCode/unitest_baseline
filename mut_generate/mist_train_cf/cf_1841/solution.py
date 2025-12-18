"""
QUESTION:
Implement the `square` function that takes another function `func` and a number `num` as arguments and returns the square of the result of `func(num)`. The `square` function should work with any function that takes one number as an argument and returns a number. 

For example, if the `multiply` function is defined as `def multiply(num): return num * num`, then `square(multiply, 4)` should return `16`. However, if the `multiply` function is defined as `def multiply(num): return num * 2`, then `square(multiply, 4)` will produce incorrect results. Identify the error in the `square` function when `multiply` function is defined as `def multiply(num): return num * 2` and correct it.
"""

def square(func, num):
    return func(num) ** 2