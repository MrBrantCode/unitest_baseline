"""
QUESTION:
Write a function `calculate_factorials` that takes a list of non-negative integers as input and returns a new list containing the factorial of each number in the input list. The function should use recursion to calculate the factorial of each number and should not use any built-in libraries or mathematical operators besides multiplication and comparison.
"""

def calculate_factorials(arr):
    def calculate_factorial(n):
        if n == 0:
            return 1
        else:
            return n * calculate_factorial(n - 1)

    return [calculate_factorial(num) for num in arr]