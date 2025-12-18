"""
QUESTION:
Write a function `find_prime_palindromes(n)` that prints the first `n` numbers that are both prime and palindromes. The function should start checking from the number 2. A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself. A palindrome is a number that remains the same when its digits are reversed.
"""

def find_prime_palindromes(n):
    """
    Prints the first n numbers that are both prime and palindromes.
    
    Args:
        n (int): The number of prime palindromes to find.
    """
    def is_prime(num):
        """Checks if a number is prime."""
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def is_palindrome(num):
        """Checks if a number is a palindrome."""
        return str(num) == str(num)[::-1]

    count = 0
    num = 2

    while count < n:
        if is_prime(num) and is_palindrome(num):
            print(num)
            count += 1
        num += 1