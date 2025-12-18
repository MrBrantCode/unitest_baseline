"""
QUESTION:
Create a function `fibonacci` to generate the Fibonacci sequence. The function should take an integer `num` and an optional dictionary `computed` as input. If `num` is less than or equal to 0, the function should print an error message and return. If `num` is 1 or 2, the function should return 0 or 1, respectively. For other values of `num`, the function should return the sum of the Fibonacci numbers at `num-1` and `num-2`. The function should use memoization to store computed values in the `computed` dictionary to prevent redundant computations. The function should be able to handle a custom range of Fibonacci sequence provided by the user.
"""

def fibonacci(num, computed = {1: 0, 2: 1}):
    if num <= 0:
        print("Incorrect input, enter a positive integer")
        return
    if num not in computed:
        computed[num] = fibonacci(num - 1, computed) + fibonacci(num - 2, computed)
    return computed[num]