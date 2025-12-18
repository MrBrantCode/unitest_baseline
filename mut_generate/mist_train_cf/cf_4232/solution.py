"""
QUESTION:
Write a function named `find_primes` that takes no arguments and returns a tuple. The function should find all prime numbers between 2000 and 3500 (both included) that are divisible by 3 and 5 but not a multiple of 7. The first element of the tuple should be a list of the prime numbers found and the second element should be the sum of those prime numbers.
"""

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

def find_primes():
    primes = []
    sum_of_primes = 0

    for num in range(2000, 3501):
        if num % 3 == 0 and num % 5 == 0 and num % 7 != 0:
            if is_prime(num):
                primes.append(num)
                sum_of_primes += num

    return (primes, sum_of_primes)