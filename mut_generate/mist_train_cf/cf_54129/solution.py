"""
QUESTION:
Design a function called `factorial` that calculates the factorial of a given number `n`, using tail call optimization to prevent stack overflow errors for large inputs. The function should take two parameters: `n` (the input number) and an optional accumulator parameter `acc` with a default value of 1. Implement the function in Python, considering its limitations in supporting tail call optimization.
"""

def factorial(n, acc=1):
    if n == 0:
        return acc
    else:  
        return factorial(n-1, n*acc)