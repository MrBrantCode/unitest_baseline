"""
QUESTION:
Write a function `sum_of_primes_and_fibonacci` that takes an array of integers as input and returns the sum of all positive prime numbers and Fibonacci numbers in the array. The function should exclude any negative numbers from the calculation.
"""

def entrance(numbers):
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_fibonacci(n):
        a, b = 0, 1
        while a < n:
            a, b = b, a + b
        return a == n

    total_sum = 0
    for num in numbers:
        if num > 0:
            if is_prime(num) or is_fibonacci(num):
                total_sum += num
    return total_sum