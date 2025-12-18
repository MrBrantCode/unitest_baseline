"""
QUESTION:
Write a function named `prime_advanced_sum` that takes two positive integers `n` and `k` as input. The function should return the cumulative sum of all n-digit prime numbers whose individual digit sum is also a prime number, not capable of being evenly divided by the number 5, and the number itself is not divisible by `k`. The function should exclude numbers with an even quantity of digits.
"""

def prime_advanced_sum(n, k):
    """
    Assumes n and k are positive integers, n-digit prime numbers are computed
    the cumulative sum of whose individual digit sum is also a prime number, not capable of
    being evenly divided by the number 5
    """
    def is_prime(num):
        if num < 2 or (num % 2 == 0 and num > 2): 
            return False
        return all(num % i for i in range(3, int(num**0.5) + 1, 2))

    def prime_digit_sum(num):
        digit_sum = sum(int(digit) for digit in str(num))
        return is_prime(digit_sum) and digit_sum % 5 != 0

    start = 10**(n - 1)
    end = 10**n
    prime_sum = 0

    for num in range(start, end):
        if n % 2 != 1:
            continue
        if is_prime(num) and prime_digit_sum(num) and num % k != 0:
            prime_sum += num
    return prime_sum