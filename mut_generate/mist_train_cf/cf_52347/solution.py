"""
QUESTION:
Create two functions, `recursiveFibonacci` and `dynamicFibonacci`, to compute the n-th Fibonacci series value using recursive and dynamic programming approaches, respectively. 

These functions should handle error cases for non-integer and negative indices. Implement the functions such that they return the Fibonacci series value for a given non-negative integer n, where n is the position within the Fibonacci sequence.
"""

def fibonacci(n):
    # Checking for integer values
    if not isinstance(n, int):
        print ("Error! Only integers are allowed")
        return None

    # Checking for negative index values
    if n < 0:
        print ("Error! Negative values are not allowed")
        return None

    # Dynamic Programming approach to solve fibonacci sequence
    fib = [0, 1] + [0]*(n-1)
    for i in range(2, n+1):
        fib[i] = fib[i-1] + fib[i-2]
    return fib[n]