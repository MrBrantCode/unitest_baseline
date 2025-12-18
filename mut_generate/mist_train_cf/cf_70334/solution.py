"""
QUESTION:
Create two functions: `fibonacci_up_to_n(n)` and `is_fibonacci(number)`. 

The function `fibonacci_up_to_n(n)` should return a list of Fibonacci numbers up to the given number `n`. 

The function `is_fibonacci(number)` should return a boolean value indicating whether the given number is a Fibonacci number or not. 

Restrictions: `n` can be up to 10^6.
"""

def fibonacci_up_to_n(n):
    fib = [0, 1]
    while fib[-1] <= n:
        fib.append(fib[-1] + fib[-2])
    return fib[:len(fib)-1]


def is_fibonacci(number):
    import math
    val1 = 5 * number * number + 4
    val2 = 5 * number * number - 4
    return val1 == int(math.sqrt(val1)) * int(math.sqrt(val1)) or val2 == int(math.sqrt(val2)) * int(math.sqrt(val2))