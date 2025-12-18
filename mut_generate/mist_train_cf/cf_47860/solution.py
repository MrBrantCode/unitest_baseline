"""
QUESTION:
Write a function named `fibonacci(n)` that generates the first `n` elements of the Fibonacci sequence, then use it to calculate the first 10 values of the sequence and print them in descending order. The function should take an integer `n` as input, where `n` is a positive integer, and it should use a loop structure to calculate the sequence values.
"""

def fibonacci(n):
    # first two values in Fibonacci sequence
    fib_seq = [0, 1]

    # generate the rest of the sequence up to the nth element
    for i in range(2, n):
        next_value = fib_seq[i-1] + fib_seq[i-2]
        fib_seq.append(next_value)

    return fib_seq[::-1]  # return the sequence in descending order