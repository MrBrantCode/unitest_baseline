"""
QUESTION:
Write a function `avg_of_primes` that calculates the average of all prime numbers in a given array of integers. The function should handle cases where there are no prime numbers in the array.
"""

def avg_of_primes(arr):
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    prime_sum = 0
    prime_count = 0

    for num in arr:
        if is_prime(num):
            prime_sum += num
            prime_count += 1

    return prime_sum / prime_count if prime_count > 0 else 0