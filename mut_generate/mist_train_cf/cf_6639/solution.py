"""
QUESTION:
Implement the function `fibonacci(n: int) -> int` to calculate the Nth term of the Fibonacci sequence using dynamic programming, where `n` is a positive integer. The function should have a time complexity of O(n) and a space complexity of O(n). It should handle values of `n` up to 10^6 efficiently and return an error message for negative or non-integer values of `n`.
"""

def fibonacci(n: int) -> int:
    # Check for negative values of n
    if n < 0:
        return "Error: n must be a positive integer"

    # Check for non-integer values of n
    if not isinstance(n, int):
        return "Error: n must be an integer"

    # Use dynamic programming approach to calculate the Fibonacci sequence
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        fib_sequence = [0, 1]
        for i in range(2, n+1):
            fib_sequence.append(fib_sequence[i-1] + fib_sequence[i-2])
        return fib_sequence[n]