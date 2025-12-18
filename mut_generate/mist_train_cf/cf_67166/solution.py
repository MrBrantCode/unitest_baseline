"""
QUESTION:
Implement a function called `Fibonacci` that generates the nth Fibonacci number and returns the result. The function should use memoization to store the results of previous calculations, handle non-integer data types, and handle negative integers. The function should take an integer `n` as input and return an integer or an error message if the input is invalid. The function should not take any additional inputs other than `n` and an optional memoization dictionary.
"""

def Fibonacci(n, memo={}):
    if n in memo:
        return memo[n]
    
    if type(n) != int or n < 0:
        return "Error: Input should be a non-negative integer."
    
    elif n < 2:
        result = n
    else:
        result = Fibonacci(n-1, memo) + Fibonacci(n-2, memo)
    
    memo[n] = result
    
    return result