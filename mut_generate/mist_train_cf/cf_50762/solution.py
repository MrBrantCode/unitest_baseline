"""
QUESTION:
Create a Python function named `factorial` to calculate the factorial of a given integer `n` using recursion, displaying the intermediate steps involved in the calculation. The function should handle the base case where `n` is 0. Additionally, modify the function to count the number of recursive calls made and analyze the time complexity of the function. Assume the input `n` is a non-negative integer.
"""

calls = 0
def factorial(n):
    global calls
    calls += 1
    if n == 0:
        return 1
    else:
        result = n * factorial(n - 1)
        print(f"factorial({n}) = {n} * factorial({n-1}) = {result}")
        return result