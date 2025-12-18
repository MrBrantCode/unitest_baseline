"""
QUESTION:
Implement a function named `is_prime_palindrome` that takes an integer `num` as input and returns a boolean indicating whether the number is both a prime number and a palindrome. The function should return True if the number is a prime palindrome and False otherwise.
"""

def is_prime_palindrome(num):
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_palindrome(n):
        num_str = str(n)
        return num_str == num_str[::-1]

    return is_prime(num) and is_palindrome(num)