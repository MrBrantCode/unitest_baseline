"""
QUESTION:
Find the Big O notation of a function named `recursive_function(n)` that takes a positive integer `n` as input and must be implemented recursively.
"""

def entance(n):
    if n <= 0:
        return
    else:
        # O(1) operation
        print("Hello!")
        # Recursive call with input size reduced by 1
        entance(n - 1)