"""
QUESTION:
Write a function `sum_palindromic_primes` that takes a list of integers as input and returns the sum of all palindromic prime numbers with a digit sum greater than 10. If no such numbers exist in the list, return 0. Assume the input list contains only integers.
"""

def sum_palindromic_primes(nums):
    def is_palindrome(n):
        return str(n) == str(n)[::-1]

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                return False
        return True

    def digit_sum(n):
        return sum(int(d) for d in str(n))

    result = 0
    for n in nums:
        if is_palindrome(n) and is_prime(n) and digit_sum(n) > 10:
            result += n
    return result