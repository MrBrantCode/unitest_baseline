"""
QUESTION:
Create a function `generate_fibonacci(n)` that generates the Fibonacci sequence up to a given number `n`, where `n` is greater than or equal to 2, and returns the sequence. Also, create helper functions `calculate_sum(sequence)`, `is_prime(n)`, and `find_prime_factors(n)` to calculate the sum of the sequence, check if a number is prime, and find the prime factors of a number respectively.
"""

def generate_fibonacci(n):
    fibonacci_seq = [0, 1]  # Initialize the Fibonacci sequence
    while fibonacci_seq[-1] <= n:
        next_num = fibonacci_seq[-1] + fibonacci_seq[-2]
        if next_num <= n:
            fibonacci_seq.append(next_num)
        else:
            break
    return fibonacci_seq