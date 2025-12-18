"""
QUESTION:
Write a function called `fibonacci_reverse` that takes an integer `n` as input and returns the Fibonacci sequence up to the `n`-th term in reverse order, considering Python's 0-based indexing. The function should generate the Fibonacci sequence starting from the base list [0, 1] and then reverse it.
"""

def fibonacci_reverse(n):
    # define base list for Fibonacci sequence
    fibonacci_seq = [0, 1]
    
    # generate Fibonacci sequence
    while len(fibonacci_seq) <= n:
        fibonacci_seq.append(fibonacci_seq[-1] + fibonacci_seq[-2])
        
    # return reversed Fibonacci sequence
    return fibonacci_seq[::-1]