"""
QUESTION:
Create a function called `factorial` that computes the product of numbers from 1 to n, where n can be a large number (1000 or more). The function should handle edge cases such as negative inputs and zero, and optimize for time and space complexity.
"""

def factorial(n):
    # Handling Edge Cases
    if n<0:
        return "Error! Factorial of a negative number doesn't exist."
    elif n==0:
        return 1
    
    result = 1
    for i in range(1, n+1): 
        result *= i
    return result