"""
QUESTION:
Create a function named `fibonacci` that generates the Fibonacci sequence up to the point where the last number in the sequence is 144 or less, without exceeding 144. The function should be implemented recursively and return a list of integers representing the Fibonacci sequence.
"""

def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [1]
    elif n == 2:
        return [1, 1]
    else:
        fib_seq = fibonacci(n - 1)
        fib_seq.append(fib_seq[-1] + fib_seq[-2])
        return fib_seq

def fib_sequence_up_to_144():
    n = 1
    while True:
        if fibonacci(n)[-1] > 144:
            return fibonacci(n - 1)
        else:
            n += 1