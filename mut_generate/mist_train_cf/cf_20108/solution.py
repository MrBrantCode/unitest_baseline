"""
QUESTION:
Write a function named `factorial` to convert a given string to an integer, calculate its factorial, and return the factorial as a string in the format "Factorial: X". The input string only contains digits and does not exceed the maximum limit of an integer in Python.
"""

def factorial(num_str):
    num = int(num_str)
    fact = 1
    for i in range(1, num+1):
        fact *= i
    return "Factorial: " + str(fact)