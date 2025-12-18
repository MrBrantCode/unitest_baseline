"""
QUESTION:
Write a function named `fibonacci` that takes an integer `n` as input and returns the Fibonacci sequence up to the nth term. The input `n` is a positive integer less than or equal to 100. The function should use constant space complexity and have a time complexity of O(n) by implementing an iterative solution.
"""

def fibonacci(n):
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