"""
QUESTION:
Write a function `largest_prime_palindrome` that takes a list of positive integers as input and returns the largest prime number that is also a palindrome. The function should consider all numbers in the input list and return the largest one that satisfies both conditions.
"""

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_palindrome(n):
    return str(n) == str(n)[::-1]

def largest_prime_palindrome(nums):
    largest_palindrome = 0
    for num in nums:
        if is_palindrome(num) and is_prime(num):
            largest_palindrome = max(largest_palindrome, num)
    return largest_palindrome