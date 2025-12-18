"""
QUESTION:
Write a function `longest_consecutive_primes(numbers)` that takes a list of integers as input and returns the longest consecutive sequence of prime numbers in the list. The function should assume that the input list contains only integers and does not need to handle any exceptions. The function should also not take any other parameters besides the list of integers.
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