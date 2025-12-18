"""
QUESTION:
Create a function named `fibonacci` that takes a prime number `n` greater than 10^6 as input and returns the first `n` elements of the Fibonacci sequence. The function should have a time complexity of O(n) and space complexity of O(1).
"""

def fibonacci(n):
    if n <= 0:
        return []
    
    fib_sequence = [0, 1]
    
    if n <= 2:
        return fib_sequence[:n]
    
    a, b = 0, 1
    for _ in range(2, n):
        a, b = b, a + b
        fib_sequence.append(b)
    
    return fib_sequence