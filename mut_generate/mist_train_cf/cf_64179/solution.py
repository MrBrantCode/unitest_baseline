"""
QUESTION:
Create a function named `fibonacci_sequences` that takes an integer `n` as input and returns a list of `n` Fibonacci sequences, each with a length of `n`. The Fibonacci sequences should start from 0 and the maximum number in each sequence should not exceed `n-1`. If `n` is less than or equal to 0, return an empty list. 

Constraints: 1 <= n <= 50
"""

def fibonacci_sequences(n):
    if n <= 0:
        return []
    else:
        fib_sequences = []
        for _ in range(n):
            fib_sequence = [0]
            if n > 1:
                fib_sequence.append(1)
            for i in range(2, n):
                next_number = fib_sequence[i-1] + fib_sequence[i-2]
                if next_number < n:
                    fib_sequence.append(next_number)
                else:
                    break
            fib_sequences.append(fib_sequence)
        return fib_sequences