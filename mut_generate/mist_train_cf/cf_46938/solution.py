"""
QUESTION:
Create a function `factorial(n)` that calculates the factorial of a given number `n` using recursion. Additionally, define a higher-order function `apply_func(func, numbers)` that applies the given function `func` to each element in the list `numbers` and returns the results in a list. The `apply_func` function should utilize list comprehensions. Implement these functions in a way that allows for calculating the factorials of a list of numbers by passing `factorial` as an argument to `apply_func`.
"""

# Define a function to calculate a factorial using recursion.
def factorial(n):
    return 1 if n <= 1 else n * factorial(n-1)

# Define a higher-order function that takes a function and list as inputs.
def apply_func(func, numbers):
    return [func(num) for num in numbers]