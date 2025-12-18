"""
QUESTION:
Develop a function `longest_consecutive_primes` that takes a list of integers as input and returns the longest consecutive sequence of prime numbers in the list. The function should identify the longest sequence where all numbers are prime and appear consecutively in the input list. The input list can contain any integers, including negative numbers, zero, and non-consecutive prime numbers.
"""

def longest_consecutive_primes(numbers):
    def is_prime(n):
        """Return True if n is prime, else False."""
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    """Return the longest consecutive sequence of prime numbers in a list of integers."""
    longest_sequence = []
    current_sequence = []
    for num in numbers:
        if is_prime(num):
            current_sequence.append(num)
        else:
            if len(current_sequence) > len(longest_sequence):
                longest_sequence = current_sequence
            current_sequence = []
    if len(current_sequence) > len(longest_sequence):
        longest_sequence = current_sequence
    return longest_sequence