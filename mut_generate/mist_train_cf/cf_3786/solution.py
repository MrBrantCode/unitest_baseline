"""
QUESTION:
Create two recursive functions, `factorial(n)` and `fibonacci(n)`, that calculate the factorial and Fibonacci sequence of a given positive integer `n` respectively. Implement memoization to optimize the performance of these recursive functions by storing previously computed values in a dictionary. Ensure the program includes input validation to handle cases where the user enters a non-positive integer. The program should prompt the user for input and display the calculated factorial and Fibonacci sequence up to the input number.
"""

# Memoization dictionary to store previously computed values
memo = {}

def factorial(n):
    # Base case: factorial of 0 or 1 is 1
    if n == 0 or n == 1:
        return 1
    
    # Check if value is already memoized
    if n in memo:
        return memo[n]
    
    # Recursive case: compute factorial of n
    result = n * factorial(n-1)
    
    # Memoize the result
    memo[n] = result
    
    return result