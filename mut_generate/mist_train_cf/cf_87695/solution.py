"""
QUESTION:
Generate a function `fibonacci(n)` to produce the Fibonacci sequence up to the nth number using an iterative approach. The function should have a time complexity of O(n) and a space complexity of O(1), where n is the input number.
"""

def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    
    fib_seq = [0, 1]  

    for i in range(2, n):
        fib_seq.append(fib_seq[i-1] + fib_seq[i-2])
    
    return fib_seq