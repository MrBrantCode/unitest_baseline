"""
QUESTION:
Create a recursive function `fibonacci(n)` to generate the Fibonacci series up to the n-th term. The function should return a list of integers representing the Fibonacci series. The function should have a base case for when n is less than or equal to 0, and it should use recursion to calculate the Fibonacci series for n greater than 2. The time complexity of the function should be O(2^n).
"""

def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib = fibonacci(n-1)
        fib.append(fib[-1] + fib[-2])
        return fib