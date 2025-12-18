"""
QUESTION:
Create a function named `generate_list` that generates a list of numbers from 1 to n. The function should not use any built-in functions, loops, or recursion with a helper function, and the time complexity must be O(n) and the space complexity should be O(1).
"""

def generate_list(n):
    if n == 1:
        return [1]
    else:
        return generate_list(n-1) + [n]