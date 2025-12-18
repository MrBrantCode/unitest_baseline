"""
QUESTION:
Generate a function named `fibonacci` that takes an integer `n` as input and returns the Fibonacci sequence up to the nth term, where `n` is between 1 and 1000.
"""

def fibonacci(n):
    fib_seq = [0, 1]  
    
    if n <= 2:
        return fib_seq[:n]  
    
    while len(fib_seq) < n:
        next_num = fib_seq[-1] + fib_seq[-2]  
        fib_seq.append(next_num)  
        
    return fib_seq