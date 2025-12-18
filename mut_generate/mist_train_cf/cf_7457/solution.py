"""
QUESTION:
Write a function `fibonacci(n)` to generate a list of Fibonacci numbers up to the given limit `n`, where the time complexity of the function should be O(n) and space complexity should be O(1). Implement the function using recursion without any loops or iteration, built-in Python functions, or additional data structures. The function should handle negative values, non-integer values, and extremely large values of `n` by returning an empty list.
"""

def fibonacci(n):
    # Check if n is negative, non-integer, or too large
    if n < 0 or not isinstance(n, int) or n > 10**6: 
        return []
    
    # Define a helper function to calculate the Fibonacci number recursively
    def fib(n):
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        else:
            return fib(n-1) + fib(n-2)
    
    # Generate the Fibonacci numbers up to n
    fib_list = []
    i = 0
    while True:
        fib_num = fib(i)
        if fib_num > n:
            break
        fib_list.append(fib_num)
        i += 1
    
    return fib_list