"""
QUESTION:
Implement a function `fib(n, memo={})` that calculates the nth Fibonacci number and determines whether its last digit is even or odd, using memoization for efficiency. The function should return a tuple containing the nth Fibonacci number and a string indicating whether the last digit is "Even" or "Odd".
"""

def fibonacci(n, memo={}):
    """
    Function to calculate fibonacci number.
    :param n: int
    :param memo: dict
    :return: tuple
    """
    # Base case
    if n <= 0:
        return 0, "Even"
    # If Fibonacci number is already in memo, return it.
    if n in memo:
        num = memo[n]
        return num, "Even" if num % 10 % 2 == 0 else "Odd"
    
    # Recursion
    if n <= 2:
        f = 1
    else:
        f = fibonacci(n - 1, memo)[0] + fibonacci(n - 2, memo)[0]
    
    memo[n] = f
    
    return f, "Even" if f % 10 % 2 == 0 else "Odd"