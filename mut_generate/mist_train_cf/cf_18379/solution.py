"""
QUESTION:
Write a function `print_prime_numbers(numbers)` that takes a list of integers `numbers` as input, where the list contains at least 10 integers and the maximum value of the list is less than or equal to 100. The function should print all the prime numbers from the list.
"""

def print_prime_numbers(numbers):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    primes = [num for num in numbers if is_prime(num)]
    for prime in primes:
        print(prime)