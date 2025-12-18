"""
QUESTION:
Create a function `get_even_prime_and_merge` that takes two lists `l1` and `l2` as input and returns a list of even prime numbers found in both lists, sorted in descending order. The function should ignore non-prime and odd numbers, and handle negative numbers.
"""

def get_even_prime_and_merge(l1: list, l2: list):
    """Return only even prime numbers from both lists, merged and sorted in descending order."""
    
    def is_prime(x: int):
        """Helper function for checking primality of a number."""
        if x < 2:
            return False
        for i in range(2, int(x**0.5) + 1):
            if x % i == 0:
                return False
        return True

    even_prime_numbers = []
    for num in l1+l2:  # Merge the numbers from both lists into a single for loop
        if num == 2:  # 2 is the only even prime number
            even_prime_numbers.append(num)

    return sorted(even_prime_numbers, reverse=True)