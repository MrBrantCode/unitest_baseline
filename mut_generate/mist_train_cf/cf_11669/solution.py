"""
QUESTION:
Write a recursive function named `factorial` that calculates the factorial of a given non-negative integer `n` and returns a tuple containing the result and the number of times the function was called. The function should have an additional parameter `count` with a default value of 0 to keep track of the recursive calls.
"""

def entrance(n, count=0):
    # Base case: if n is 0 or 1, return 1
    if n == 0 or n == 1:
        return 1, count
    
    # Recursive case: multiply n with factorial(n-1)
    result, count = entrance(n-1, count + 1)
    
    # Multiply the result with n
    result *= n
    
    return result, count