"""
QUESTION:
Construct a function `fibonacci_series(n)` that generates a list of the first `n` Fibonacci numbers using a looping mechanism. The function should return the list of Fibonacci numbers. 

Additionally, create a function `nth_fibonacci(n)` that returns the `n`th Fibonacci number from the sequence. This function should handle edge cases where `n` is not a positive integer by returning an error message.
"""

def fibonacci_series(n):
    fib_list = [0, 1]
    while len(fib_list) < n:
        fib_list.append(fib_list[-1] + fib_list[-2])
    return fib_list

def nth_fibonacci(n):
    if n <= 0:
        return "Error: Input should be a positive integer."
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        fib_list = [0, 1]
        while len(fib_list) < n:
            fib_list.append(fib_list[-1] + fib_list[-2])
        return fib_list[-1]