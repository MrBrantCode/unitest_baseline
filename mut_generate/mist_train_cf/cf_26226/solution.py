"""
QUESTION:
Create a function `Fibonacci_sequence(length)` that generates a Fibonacci sequence of a given length. The function should return a list of integers representing the Fibonacci sequence. The sequence should start with 0 and 1, and each subsequent number should be the sum of the previous two numbers. The function should be able to handle lengths of at least 1 and greater.
"""

def Fibonacci_sequence(length): 
    fib_seq = [0, 1]
    if length == 1:
        return [0]
    elif length == 2:
        return fib_seq
    else:
        for i in range(2, length):
            fib_seq.append(fib_seq[i - 1] + fib_seq[i - 2])
        return fib_seq