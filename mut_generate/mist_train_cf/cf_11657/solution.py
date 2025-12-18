"""
QUESTION:
Write a function `fibonacci(n, memo={})` that generates the nth Fibonacci number using memoization to optimize the recursive function and avoid redundant calculations. Implement another function `print_fibonacci_sequence(num)` that prints the Fibonacci sequence up to a given number `num`. The `print_fibonacci_sequence(num)` function should use the `fibonacci(n, memo={})` function to generate the sequence and handle large numbers efficiently without causing memory overflow or excessive runtime.
"""

# Function to generate the nth Fibonacci number using memoization
def fibonacci(n, memo={}):
    if n in memo:
        return memo[n]
    elif n <= 1:
        memo[n] = n
        return n
    else:
        memo[n] = fibonacci(n-1, memo) + fibonacci(n-2, memo)
        return memo[n]

# Function to print the Fibonacci sequence up to a given number
def print_fibonacci_sequence(num):
    sequence = []
    n = 0
    while True:
        fib = fibonacci(n)
        if fib > num:
            break
        sequence.append(fib)
        n += 1
    return sequence