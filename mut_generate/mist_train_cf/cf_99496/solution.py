"""
QUESTION:
Develop a function named `longest_consecutive_primes` that takes a list of integers as input and returns the longest consecutive sequence of prime numbers within the list. The function should handle sequences at the end of the list and sequences of equal length, returning the first one encountered. Assume the input list may contain non-prime and prime numbers, and may be empty.
"""

def longest_consecutive_primes(numbers):
    """Return the longest consecutive sequence of prime numbers in a list of integers."""
    def is_prime(n):
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