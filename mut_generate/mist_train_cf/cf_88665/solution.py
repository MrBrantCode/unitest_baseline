"""
QUESTION:
Write a function `fibonacci(n)` that takes a positive integer `n` (n ≤ 100) as input and returns the Fibonacci sequence up to the nth term using an iterative solution with O(n) time complexity and constant space complexity, handling edge cases for n = 0, 1, or 2.
"""

def fib(n):
    if n == 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    
    fib_seq = [0, 1]  
    for i in range(2, n):
        fib_seq.append(fib_seq[i-1] + fib_seq[i-2])  
        
    return fib_seq