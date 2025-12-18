"""
QUESTION:
Create a function named `factorial` that calculates the factorial of a given number `n` using tail recursion. The function should have a base case and utilize an accumulator variable `acc` to optimize the recursive calls. The function should be designed such that the recursive call is the last operation, allowing for tail call optimization.
"""

def factorial(n, acc=1):
    if n == 0:
        return acc
    else:
        return factorial(n - 1, acc * n)