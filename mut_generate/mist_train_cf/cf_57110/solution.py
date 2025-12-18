"""
QUESTION:
Write a function `fib(n)` to find the nth Fibonacci number, where `n` is the index of the Fibonacci sequence. The function should start with the base case of the Fibonacci sequence (0 and 1) and return the nth Fibonacci number with the best possible time complexity.
"""

def fib(n):
    # Fast doubling Fibonacci algorithm. 
    # CF. http://www.nayuki.io/page/fast-fibonacci-algorithms

    # Returns a tuple (F(n), F(n+1)).
    def _fib(n):
        if n == 0:
            return (0, 1)
        else:
            a, b = _fib(n // 2)
            c = a * ((b << 1) - a)
            d = a * a + b * b
            if n & 1:
                # For odd n
                return (d, c + d)
            else:
                # For even n
                return (c, d)

    return _fib(n)[0]