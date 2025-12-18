"""
QUESTION:
Write a function named `fibo` that generates the first `n` numbers in the Fibonacci sequence, where each number is the sum of the two preceding ones, usually starting with 0 and 1, and returns the sequence as a list. The input to the function is `seq_length`, which is a positive integer representing the number of Fibonacci numbers to generate.
"""

def fibo(seq_length):
    fib_series = [0,1] 
    while len(fib_series) < seq_length:
        fib_series.append(fib_series[-1] + fib_series[-2])

    return fib_series