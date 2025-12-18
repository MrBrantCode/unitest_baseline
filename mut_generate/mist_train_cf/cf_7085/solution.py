"""
QUESTION:
Write a function named `sum_of_primes` that calculates the sum of all prime numbers between 1 and a given upper limit (100 in this case), excluding any prime number that is divisible by 4.
"""

def sum_of_primes(n):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    total_sum = 0
    for i in range(2, n + 1):
        if is_prime(i) and i % 4 != 0:
            total_sum += i
    return total_sum