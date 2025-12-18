"""
QUESTION:
Write a function `factorial(n, acc=1)` to calculate the factorial of a number `n` using tail recursion. The function should take an optional parameter `acc` with a default value of 1 to store the accumulated result. The function must be tail recursive, meaning the recursive call is the last operation in the function.
"""

def factorial(n, acc=1):
    if n == 0:
        return acc
    else:
        return factorial(n - 1, acc * n)