"""
QUESTION:
Write a function named `factorial` to calculate the factorial of a number `n`. The function should use tail recursion to avoid stack overflow errors. The function should take an optional parameter `acc` with a default value of 1 to accumulate the result. Implement tail recursion by making the recursive call the last operation in the function.
"""

def factorial(n, acc=1):
    if n == 0:
        return acc
    else:
        return factorial(n - 1, acc * n)