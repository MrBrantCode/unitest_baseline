"""
QUESTION:
Write a program with two functions, `iterative_factorial(x)` and `recursive_factorial(x)`, to calculate the factorial of a given integer `x`. Compare the execution times of both methods. Ensure the program can handle large integer inputs by using an iterative approach or adjusting the recursion limit. Implement the functions in a way that allows for execution time measurement.
"""

def iterative_factorial(x):
    result = 1
    for i in range(1, x + 1):
        result *= i
    return result

def recursive_factorial(x):
    if x == 1 or x == 0:
        return 1
    else:
        return x * recursive_factorial(x - 1)