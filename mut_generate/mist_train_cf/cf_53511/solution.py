"""
QUESTION:
Create a function named `get_evens_and_primes` that takes two lists of integers as input and returns a list of numbers that are either even or prime, merged and sorted in descending order, excluding negative numbers. 

The function should use helper functions to check for prime numbers and to merge and sort the lists.
"""

def get_evens_and_primes(l1: list, l2: list):
    """Return only even and prime numbers from both lists, merged and sorted in descending order.
    """
    def is_prime(n: int):
        """Check if a number is prime."""
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    def merge_and_sort(m: list, n: list):
        """Merge two lists and sort them in descending order."""
        merged_list = m + n
        merged_list.sort(reverse=True)
        return merged_list

    even_and_prime_numbers = []
    for num in l1 + l2:  # Merged the lists here to avoid code duplication
        if num >= 0:  # Exclude negative numbers
            if num % 2 == 0 or is_prime(num):  # Check for prime numbers too
                even_and_prime_numbers.append(num)

    return merge_and_sort(even_and_prime_numbers, [])  # No need for a second list so passed an empty list