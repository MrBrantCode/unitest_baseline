"""
QUESTION:
Calculate the sum of all prime numbers from 1 to a given number 'n', excluding numbers that are divisible by both 2 and 3, and store the result in the variable 'total'. Implement a helper function 'is_prime(num)' to check if a number is prime.
"""

def calculate_prime_sum(n):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    total = 0
    for i in range(1, n+1):
        if i % 2 == 0 and i % 3 == 0:
            continue
        elif is_prime(i):
            total += i
    return total