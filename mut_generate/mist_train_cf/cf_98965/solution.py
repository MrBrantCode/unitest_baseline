"""
QUESTION:
Write a function `find_largest_prime_in_sequence` that generates a sequence by concatenating the digits of the previous term, starting from 2. The function should find and return the largest prime number in this sequence, given the number of terms `num_terms` and an upper limit `limit`.
"""

def find_largest_prime_in_sequence(num_terms, limit):
    largest_prime = None
    current_term = '2'
    for i in range(num_terms):
        if int(current_term) > limit:
            break
        if is_prime(int(current_term)):
            largest_prime = int(current_term)
        current_term += current_term[-1]
    return largest_prime

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True