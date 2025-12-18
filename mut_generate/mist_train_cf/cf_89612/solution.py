"""
QUESTION:
Write a function `sum_of_palindromic_primes(n)` that takes an integer n as input and returns the sum of the first n prime numbers that are also palindromes. The function should have a time complexity of O(n^3) and a space complexity of O(n).
"""

def sum_of_palindromic_primes(n):
    def is_palindrome(num):
        return str(num) == str(num)[::-1]

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    count = 0
    total = 0
    num = 2
    while count < n:
        if is_palindrome(num) and is_prime(num):
            total += num
            count += 1
        num += 1
    return total