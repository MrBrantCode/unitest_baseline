"""
QUESTION:
Write a function `calculate_factorials(arr)` that calculates the factorial of each number in the list `arr` using recursion, without using any built-in libraries or mathematical operators. The function should return a new list containing the factorial of each number in the input list.
"""

def calculate_factorials(arr):
    def factorial(n):
        if n == 0:
            return 1
        else:
            return n * factorial(n - 1)

    result = []
    for num in arr:
        result.append(factorial(num))
    return result