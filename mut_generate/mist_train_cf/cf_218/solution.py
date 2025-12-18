"""
QUESTION:
Write a function `sum_even_primes` that takes a list of at least 15 positive integers, each a prime number less than or equal to 100, and returns the sum of all even prime numbers in the list if the number of even primes is greater than the number of odd primes and the sum is greater than 200. Otherwise, return "No sum found".
"""

def sum_even_primes(lst):
    """
    This function calculates the sum of all even prime numbers in a given list.
    It returns the sum if the number of even primes is greater than the number of odd primes and the sum is greater than 200.
    Otherwise, it returns "No sum found".

    Parameters:
    lst (list): A list of at least 15 positive integers, each a prime number less than or equal to 100.

    Returns:
    int or str: The sum of even prime numbers if conditions are met, "No sum found" otherwise.
    """

    # Filter the prime numbers to get only the even and odd ones
    even_primes = [p for p in lst if p % 2 == 0]
    odd_primes = [p for p in lst if p % 2 != 0]

    # Check if the number of even primes is greater than the number of odd primes
    if len(even_primes) > len(odd_primes):
        # Calculate the sum of the even prime numbers
        prime_sum = sum(even_primes)
        # Check if the sum is greater than 200
        if prime_sum > 200:
            return prime_sum
    return "No sum found"