"""
QUESTION:
Write a function named `fibonacci_selector` that takes an index as input and returns the corresponding Fibonacci number. The Fibonacci sequence should contain numbers up to the 100th Fibonacci number. The function should also handle invalid inputs (non-integer or negative) and out-of-range indexes (beyond the 100th Fibonacci number) by returning a descriptive error message.
"""

def fibonacci_selector(index):
    if isinstance(index, int) and index >= 0:
        fib_seq = [0, 1]
        for i in range(2, 101):
            fib_seq.append(fib_seq[i-1] + fib_seq[i-2])
        if index < len(fib_seq):
            return fib_seq[index]
        else:
            return 'Index out of range. Please enter a valid index.'
    else:
        return 'Invalid input. Please enter a positive integer.'