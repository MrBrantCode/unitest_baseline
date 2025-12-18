"""
QUESTION:
Implement a function called `is_prime_palindrome(num)` that checks if the input number is both a prime number and a palindrome. The function should return a boolean value indicating whether the number is a prime palindrome or not.
"""

def is_prime_palindrome(num):
    def is_prime(num):
        if num <= 1:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    def is_palindrome(num):
        num_str = str(num)
        return num_str == num_str[::-1]

    return is_prime(num) and is_palindrome(num)