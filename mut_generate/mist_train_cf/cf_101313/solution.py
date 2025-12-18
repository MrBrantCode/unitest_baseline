"""
QUESTION:
Write a function called `recursive_hello_world` that takes an integer `n` as input and returns a string containing "Hello World" repeated `n` times, using a recursive function and nested loop structure without any built-in Python functions, with the output string stored in a variable before being printed or returned.
"""

def recursive_hello_world(n):
    return 'Hello World\n' * n + (recursive_hello_world(n-1) if n > 1 else '')