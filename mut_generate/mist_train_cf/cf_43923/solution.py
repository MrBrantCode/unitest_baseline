"""
QUESTION:
Write a recursive function `inverse_fib(n, a, b)` that counts down from `n` to 0 in an inverse Fibonacci sequence progression, where `a` and `b` are the first two numbers of the Fibonacci sequence (initially 0 and 1). The function should take no additional input other than the initial call, and `a` and `b` should default to 0 and 1 if not provided.
"""

def inverse_fib(n, a=0, b=1):
    # base case
    if n < a:
        return
    # recursive case
    else:
        print(n)
        return inverse_fib(n-a-b, b, a+b)