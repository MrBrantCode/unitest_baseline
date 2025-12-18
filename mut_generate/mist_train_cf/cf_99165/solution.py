"""
QUESTION:
Create a function sum_of_primes(start, end) that calculates the sum of all prime numbers within a specified range. The function should take two integer parameters, start and end, and return the sum of all prime numbers between these two points. The function should handle edge cases such as non-numeric or negative inputs, and be efficient enough to handle large range inputs.
"""

def sum_of_primes(start, end):
    # Edge cases: non-numeric values or negative inputs
    if not isinstance(start, int) or not isinstance(end, int):
        return "Inputs must be integers"
    if start < 0 or end < 0:
        return "Inputs cannot be negative"

    # Function to check if a number is prime
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    # Loop through range and sum prime numbers
    total = 0
    for n in range(start, end + 1):
        if is_prime(n):
            total += n

    return total