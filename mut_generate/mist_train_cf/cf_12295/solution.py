"""
QUESTION:
Write a function named `sum_of_primes` that calculates the sum of all prime numbers from 1 to a given positive integer `n`, excluding `n` itself. The function should use 'break' and 'continue' statements in a for loop to efficiently skip non-prime numbers and terminate the loop when the sum is greater than or equal to `n`. The time complexity should be O(n * sqrt(m)), where `n` is the given positive integer and `m` is the current number being evaluated.
"""

def sum_of_primes(n):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    prime_sum = 0
    for num in range(2, n):
        if not is_prime(num):
            continue
        prime_sum += num
        if prime_sum >= n:
            break
    return prime_sum