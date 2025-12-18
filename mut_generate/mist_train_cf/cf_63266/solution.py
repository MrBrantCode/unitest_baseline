"""
QUESTION:
Write a function named `fibonacci(n, m)` that takes two integers `n` and `m` as parameters. The function should generate a Fibonacci sequence up to the `n`th term and return the `m`th term of the sequence. The function should handle edge cases where `m` is greater than `n`, or either `n` or `m` are non-integer or negative values.
"""

def fibonacci(n, m):
    # Check if n and m are integers, and if n is greater than or equal to m
    try:
        if not isinstance(n, int) or not isinstance(m, int):
            return "Both n and m need to be whole numbers."
        if n < 0 or m < 0:
            return "Neither n nor m can be negative numbers."
        if m > n:
            return "m can't be greater than n."
        # Creating a list that starts with the first two Fibonacci numbers
        fib_seq = [0, 1]
        # Add the next n-2 Fibonacci numbers to the list
        while len(fib_seq) < n:
            fib_seq.append(fib_seq[-2] + fib_seq[-1])
        # Return the mth term of the list (adjust for zero indexing)
        return fib_seq[m-1]
    except Exception as e:
        return str(e)