"""
QUESTION:
Write a Python function named `factorial` that takes an integer `n` as input, calculates the factorial of `n` using recursion, and returns the result. The function should also calculate the summation of the factorials of all integers from 0 to `n`, inclusive, and print both the factorial and the summation to the console.
"""

def factorial(n):
    # base case
    if n == 0:
        return 1, 1
    # recursive case
    else:
        # calculate the factorial and summation of n-1
        fact_n_1, total = factorial(n-1)
        # calculate the factorial of n
        fact_n = n * fact_n_1
        # calculate the summation of factorials from 0 to n
        total += fact_n
        # print the result to the console
        print("Factorial of", n, ":", fact_n)
        print("Summation of factorials from 0 to", n, ":", total)
        return fact_n, total