"""
QUESTION:
Write a function `largest_prime_palindrome` that takes a list of positive integers as input and returns the largest prime number that is a palindrome from the given list. The function should return 0 if no prime palindrome is found.
"""

def largest_prime_palindrome(test_list):
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_palindrome(n):
        return str(n) == str(n)[::-1]

    largest_palindrome = 0
    for num in test_list:
        if is_palindrome(num) and is_prime(num):
            largest_palindrome = max(largest_palindrome, num)
    return largest_palindrome