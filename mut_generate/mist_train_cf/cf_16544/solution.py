"""
QUESTION:
Create a function named 'prime_palindrome' to generate the first 'n' prime numbers that are also palindromes. The function should return a list of these prime palindromes. Note that the prime palindrome list should only include prime numbers that read the same forwards and backwards (e.g., 121, 131).
"""

def prime_palindrome(n):
    """
    Generate the first 'n' prime numbers that are also palindromes.

    Args:
        n (int): The number of prime palindromes to generate.

    Returns:
        list: A list of the first 'n' prime palindromes.
    """
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    def is_palindrome(num):
        return str(num) == str(num)[::-1]

    prime_palindromes = []
    num = 2
    while len(prime_palindromes) < n:
        if is_prime(num) and is_palindrome(num):
            prime_palindromes.append(num)
        num += 1
    return prime_palindromes