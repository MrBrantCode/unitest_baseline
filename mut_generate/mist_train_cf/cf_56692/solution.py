"""
QUESTION:
Write a function named `fibonacci(n, dict_call_count)` that calculates the nth Fibonacci number and keeps track of the number of recursive calls performed. The function should take two parameters: `n` (the position of the Fibonacci number to calculate) and `dict_call_count` (a dictionary containing the key 'count' to store the number of recursive calls). The function should return the nth Fibonacci number and update the 'count' in `dict_call_count` accordingly.
"""

def fibonacci(n, dict_call_count):
    dict_call_count['count'] += 1 
    if n <= 1:
        return n
    else:
        return fibonacci(n-1, dict_call_count) + fibonacci(n-2, dict_call_count)