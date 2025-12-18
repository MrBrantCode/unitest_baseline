"""
QUESTION:
Create a function `calculate_cubic_values` that takes two integers `min` and `max` as input. The function should calculate and print the cubic values of all prime numbers between `min` and `max` (inclusive), and handle the case when no prime numbers exist in the given range.
"""

def calculate_cubic_values(min, max):
    def is_prime(n):
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    prime_exists = False
    for num in range(min, max + 1):
        if is_prime(num):
            prime_exists = True
            print(f"The cubic value of prime number {num} is {num**3}")
    if not prime_exists:
        print("No prime number exists in the given range.")