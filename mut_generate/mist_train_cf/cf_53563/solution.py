"""
QUESTION:
Create a function named `is_prime_and_factorial` that takes a list of integers as input. For each number in the list, check if it's a prime number, and if it is, calculate and print its factorial. A number is prime if it's greater than 1 and has no divisors other than 1 and itself. The factorial of a number n is the product of all positive integers less than or equal to n.
"""

def is_prime_and_factorial(numbers):
    def is_prime(n):
        if n <= 1:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        i = 3
        while i * i <= n:
            if n % i == 0:
                return False
            i += 2
        return True

    def factorial(n):
        fac = 1
        for i in range(1, n + 1):
            fac *= i
        return fac

    for num in numbers:
        if is_prime(num):
            print(f'{num} is prime and its factorial is {factorial(num)}')