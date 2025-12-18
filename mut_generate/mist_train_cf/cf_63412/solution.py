"""
QUESTION:
Design a recursive function `fibonacci(n)` that generates the Fibonacci sequence up to `n` numbers, where the sequence starts with the 0th and 1st elements as 0 and 1, respectively. The function should follow the recurrence relation F(n) = F(n-1) + F(n-2) and handle base cases where `n` is less than or equal to 0 (returning an empty list), `n` equals 1 (returning `[0]`), and `n` equals 2 (returning `[0, 1]`).
"""

def fibonacci(n):
    if n <= 0:  
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0,1]
    else:
        fib_sequence = fibonacci(n-1) 
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
        return fib_sequence