"""
QUESTION:
Write a function named `fibonacci_numbers` that takes an integer `limit` as input and returns a list of Fibonacci numbers within the range of 1 to the given `limit`. The list should be generated iteratively, starting from 0 and 1, and should not include numbers that exceed the specified limit.
"""

def fibonacci_numbers(limit):
    fib_seq = [0, 1]
    while True:
        new_number = fib_seq[-1] + fib_seq[-2]
        if new_number > limit:
            break
        fib_seq.append(new_number)
    return fib_seq[1:]