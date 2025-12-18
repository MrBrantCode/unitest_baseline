"""
QUESTION:
Create a function `even_fibonacci_sum(limit)` that takes an integer `limit` as input and returns the sum of all even Fibonacci numbers less than or equal to the given limit.
"""

def even_fibonacci_sum(limit):
    # Initialize variables to store the Fibonacci sequence and the sum of even numbers
    fib_sequence = [0, 1]
    even_sum = 0

    # Generate Fibonacci sequence up to the limit
    while True:
        next_fib = fib_sequence[-1] + fib_sequence[-2]
        if next_fib > limit:
            break
        fib_sequence.append(next_fib)

    # Calculate the sum of even Fibonacci numbers
    for num in fib_sequence:
        if num % 2 == 0:
            even_sum += num

    return even_sum