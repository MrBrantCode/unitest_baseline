"""
QUESTION:
Write a function called `find_twin_primes` that finds all twin prime pairs between 1 and a given upper limit (not inclusive). A twin prime pair is defined as two prime numbers that are two apart from each other. The function should exclude the prime numbers 2 and 3.
"""

def find_twin_primes(limit):
    """
    Finds all twin prime pairs between 1 and a given upper limit (not inclusive).
    
    A twin prime pair is defined as two prime numbers that are two apart from each other.
    The function excludes the prime numbers 2 and 3.

    Args:
        limit (int): The upper limit (not inclusive) for finding twin prime pairs.

    Returns:
        list: A list of tuples, where each tuple contains a twin prime pair.
    """
    def is_prime(num):
        """Helper function to check if a number is prime."""
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    twin_primes = []
    for num in range(4, limit):
        if is_prime(num) and is_prime(num + 2):
            twin_primes.append((num, num + 2))
    return twin_primes