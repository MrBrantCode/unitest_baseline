"""
QUESTION:
Implement a recursive function named `recursive_function` that takes an integer `n` as input and prints "Hello!" `n` times. The function must be implemented recursively, with each recursive call reducing the input size by 1 until `n` becomes 0 or negative.
"""

def recursive_function(n):
    if n <= 0:
        return
    else:
        print("Hello!")
        recursive_function(n - 1)