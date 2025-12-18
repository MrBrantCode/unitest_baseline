"""
QUESTION:
Generate a function named `generate_list` that returns a list of integers from 1 to n. The function should not use any built-in functions or libraries and should have a time complexity of O(n). Note that the solution provided above does not meet the original space complexity requirement of O(1), which is still unresolved.
"""

def generate_list(n):
    if n == 1:
        return [1]
    else:
        return generate_list(n-1) + [n]