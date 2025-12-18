"""
QUESTION:
Write a Python program that includes the following functions: 
- `is_prime(n)`: takes an integer `n` as input and returns a boolean indicating whether `n` is a prime number or not.
- `is_palindrome(n)`: takes an integer `n` as input and returns a boolean indicating whether `n` is a palindrome number or not.

The program should use these functions to find all prime numbers between 1000 and 2000 (inclusive), calculate the sum of these prime numbers, and count the number of palindromic prime numbers among them. The program should then print the sum of the prime numbers and the count of the palindromic prime numbers.
"""

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_palindrome(n):
    return str(n) == str(n)[::-1]