"""
QUESTION:
Create a function `print_prime_palindromes(n)` that prints all prime numbers between 0 and a given number `n` that are also palindromes. The solution should be optimized for time complexity. The function should use a while loop to iterate over the numbers and check if each number is both prime and a palindrome.
"""

import math

def print_prime_palindromes(n):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, math.isqrt(num) + 1):
            if num % i == 0:
                return False
        return True

    def is_palindrome(num):
        rev = 0
        temp = num
        while temp > 0:
            dig = temp % 10
            rev = rev * 10 + dig
            temp = temp // 10
        return num == rev

    i = 0
    while i <= n:
        if is_prime(i) and is_palindrome(i):
            print(i)
        i += 1