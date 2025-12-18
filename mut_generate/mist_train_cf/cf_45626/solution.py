"""
QUESTION:
Design a function called `factorial(n)` to calculate the factorial of a number using recursion. This function should have a base case to handle the input of 0 and a recursive case to handle other inputs. Analyze the time complexity of this function using the Master Theorem or alternative approaches.
"""

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)