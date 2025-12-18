"""
QUESTION:
Write a function `get_prime_numbers` that takes a list of integers as input and returns two values: a list of prime numbers from the input list and the sum of these prime numbers. A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself.
"""

def get_prime_numbers(numbers):
    """
    Function to filter prime numbers from a list of integers and return the sum of these prime numbers.
    """
    def is_prime(n):
        """
        Function to check if a number is prime.
        """
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    prime_numbers = []
    prime_sum = 0
    for number in numbers:
        if is_prime(number):
            prime_numbers.append(number)
            prime_sum += number
    return prime_numbers, prime_sum