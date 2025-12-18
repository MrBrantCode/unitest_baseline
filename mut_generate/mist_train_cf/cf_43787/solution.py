"""
QUESTION:
Write a function `categorize_primes` that takes a range of positive integers defined by `range_start` and `range_end` (exclusive), and categorizes prime numbers within this range into two lists: `single_digit_primes` and `multi_digit_primes`. The function should efficiently handle ranges up to 10^6 and return the two lists of prime numbers.
"""

def categorize_primes(range_start, range_end):
    def is_prime(n):
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    single_digit_primes = []
    multi_digit_primes = []
    for num in range(range_start+1, range_end):
        if is_prime(num):
            if num < 10:
                single_digit_primes.append(num)
            else:
                multi_digit_primes.append(num)
    return single_digit_primes, multi_digit_primes