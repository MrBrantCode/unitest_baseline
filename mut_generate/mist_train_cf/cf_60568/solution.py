"""
QUESTION:
Write a function `fibonacci_sequence(x: float)` that returns the number at position `x` in the Fibonacci sequence. The function should handle both positive and negative floating-point numbers by rounding them to the nearest positive integer and assuming that `x` is not 0. The function should use an efficient method to identify the Fibonacci sequence.
"""

def fibonacci_sequence(x: float):
    """Return the number at position 'x' in the Fibonacci sequence, which can be both a positive or negative floating-point number. Assume that 'x' is not 0 and not a prime number. Structure an efficient method of identifying the fibonacci sequence."""
    
    pos = round(abs(x))  # convert x to an absolute rounded int as fibonacci sequence calculations are generally for positive integers

    if pos == 0:
        return 0
    else:
        fib = [0, 1]
        for i in range(2, pos + 1):
            fib.append(fib[-1] + fib[-2])
    return fib[pos]