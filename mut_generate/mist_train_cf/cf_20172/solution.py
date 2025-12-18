"""
QUESTION:
Design a function to find all numbers between 0 and 100 that are divisible by both 3 and 5, and also prime numbers. The function should print these numbers and return their sum. The function name should be `is_prime()`.
"""

def is_prime_and_divisible(num):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    total_sum = 0
    for i in range(num + 1):
        if i % 3 == 0 and i % 5 == 0 and is_prime(i):
            print(i)
            total_sum += i
    return total_sum