"""
QUESTION:
Write a function named `print_prime_numbers` that takes an integer `n` as input and prints all prime numbers between 1 and `n` (inclusive).
"""

def print_prime_numbers(n):
    def check_prime(num):
        if num == 1:
            return False
        for i in range(2, num):
            if num % i == 0:
                return False
        return True
    for num in range(1, n + 1):
        if check_prime(num):
            print(num)