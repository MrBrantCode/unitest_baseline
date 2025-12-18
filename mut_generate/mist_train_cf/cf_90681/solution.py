"""
QUESTION:
Create a program that defines a function named `find_primes_and_palindromic_primes` to display all prime numbers and palindromic primes within a given range `a` to `b` (inclusive). The function should take two integers `a` and `b` as input and print out the prime numbers and palindromic primes separately. The input range `a` and `b` are guaranteed to be positive integers.
"""

def find_primes_and_palindromic_primes(a, b):
    """
    This function prints all prime numbers and palindromic primes within a given range a to b (inclusive).

    Parameters:
    a (int): The start of the range (inclusive).
    b (int): The end of the range (inclusive).
    """
    
    def is_prime(num):
        """
        Checks if a number is prime.

        Parameters:
        num (int): The number to check.

        Returns:
        bool: True if the number is prime, False otherwise.
        """
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    def is_palindrome(num):
        """
        Checks if a number is palindromic.

        Parameters:
        num (int): The number to check.

        Returns:
        bool: True if the number is palindromic, False otherwise.
        """
        return str(num) == str(num)[::-1]

    print("Prime Numbers:")
    for num in range(a, b+1):
        if is_prime(num):
            print(num)

    print("\nPalindromic Primes:")
    for num in range(a, b+1):
        if is_prime(num) and is_palindrome(num):
            print(num)