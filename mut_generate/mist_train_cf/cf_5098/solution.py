"""
QUESTION:
Write a function `fibonacci(n)` that generates the Fibonacci sequence up to the nth number, where n is a given integer. The function should have a time complexity of O(n) and a space complexity of O(1), and should only generate the sequence when n is a prime number between 100 and 1000 (exclusive).
"""

def fibonacci(n):
    if not (100 < n < 1000 and all(n % i != 0 for i in range(2, int(n**0.5) + 1))):
        return []
    
    fib_seq = [0, 1]
    while len(fib_seq) < n:
        fib_seq.append(fib_seq[-1] + fib_seq[-2])
    return fib_seq