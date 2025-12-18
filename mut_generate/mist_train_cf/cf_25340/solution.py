"""
QUESTION:
Write a recursive function called 'recursive_function' that demonstrates how recursion breaks down complex problems into simpler subproblems. Implement this function in Python without any arguments.
"""

def recursive_function(n=10):
    # Base case
    if n == 0:
        return
    else:
        print(n)
        recursive_function(n-1)