"""
QUESTION:
Create a function `fibonacci_sum_greater_than(n)` that generates a Fibonacci sequence where the sum of the sequence is greater than a given number `n` and only includes even numbers in the sequence. The sequence should start with the first two even numbers in the Fibonacci sequence (0 and 2). If the next Fibonacci number is odd, it should be incremented by 1 to make it even before adding it to the sequence.
"""

def fibonacci_sum_greater_than(n):
    sequence = [0, 2]  # Initial sequence with first two even numbers
    while sum(sequence) <= n:
        next_num = sequence[-1] + sequence[-2]  # Compute next Fibonacci number
        if next_num % 2 == 0:  # Only add even numbers to the sequence
            sequence.append(next_num)
        else:  # Skip odd numbers and add the next even number instead
            sequence.append(next_num + 1)
    return sequence