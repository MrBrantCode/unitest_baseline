"""
QUESTION:
Write a function named `group_primes` that takes a list of integers as input. The function should return a dictionary where the keys are the prime numbers from the input list and the values are lists containing the key itself. The function should consider the absolute value of each number when determining if it's prime.
"""

def group_primes(numbers):
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    primes = {num: [num] for num in numbers if is_prime(abs(num))}
    return primes