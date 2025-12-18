"""
QUESTION:
Write a function named `print_fibonacci_sequence` that takes an integer `n` as input. The function should print the first `n` numbers in the Fibonacci sequence, where the sequence starts with 0 and 1, and each subsequent number is the sum of the two preceding ones. If `n` is less than or equal to 0, the function should not print anything.
"""

def print_fibonacci_sequence(n):
    if n <= 0:
        return
    
    fib_sequence = [0, 1]
    if n == 1:
        print(fib_sequence[0])
    elif n == 2:
        print(fib_sequence[0], fib_sequence[1])
    else:
        print(fib_sequence[0], fib_sequence[1], end=", ")
        for i in range(2, n):
            fib_sequence.append(fib_sequence[i-1] + fib_sequence[i-2])
            print(fib_sequence[i], end=", ")
        print()