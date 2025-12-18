"""
QUESTION:
Create a function named `find_prime_and_divisor_sum` that takes a list of integers as input, identifies the prime numbers in the list, and for each prime number, calculates and returns the sum of its divisors. The function should not take any arguments other than the list of integers. The list of integers is predefined as `[2, 3, 4, 5, 6, 7, 8, 9, 10]`.
"""

def find_prime_and_divisor_sum(numbers):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def sum_of_divisors(n):
        divisor_sum = 0
        for i in range(1, n + 1):
            if n % i == 0:
                divisor_sum += i
        return divisor_sum

    prime_divisor_sums = []
    for num in numbers:
        if is_prime(num):
            prime_divisor_sums.append((num, sum_of_divisors(num)))
    return prime_divisor_sums