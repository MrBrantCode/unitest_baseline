"""
QUESTION:
Write a function named `smallest_prime_and_positions` that takes a list of integers as input and returns the smallest prime number in the list along with its positions. If there are multiple instances of the smallest prime number, return all of their positions. If the list does not contain any prime numbers, return a message indicating this. The function should be optimized to handle lists of size up to 10,000 elements.
"""

def smallest_prime_and_positions(lst):
    """Find the smallest prime number in the list and its positions"""
    def is_prime(n):
        """Check if the number is prime"""
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    prime_positions = {}
    smallest_prime = float('inf')
    for i, n in enumerate(lst):
        if is_prime(n):
            if n not in prime_positions:
                prime_positions[n] = []
            prime_positions[n].append(i)
            smallest_prime = min(smallest_prime, n)
    if smallest_prime == float('inf'):
        return "No prime numbers found in the list"
    return f"Smallest prime number is {smallest_prime} at positions {prime_positions[smallest_prime]}"