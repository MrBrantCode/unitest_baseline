"""
QUESTION:
Create a function `check_sum_primes` that takes a range defined by two integers `start` and `end`, and returns a list of prime numbers within this range whose sum of digits is also a prime number. The range is inclusive and 1 <= start <= end <= 100.
"""

def check_sum_primes(start, end):
    def check_prime(n):
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

    primes = []
    for num in range(start, end + 1):
        if check_prime(num):
            digits_sum = sum([int(d) for d in str(num)])
            if check_prime(digits_sum):
                primes.append(num)
    return primes