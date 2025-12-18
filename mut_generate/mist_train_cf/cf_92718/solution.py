"""
QUESTION:
Create a function named `get_prime_numbers` that takes a list of integers as input and returns a new list containing only the prime numbers from the original list. The function should consider a prime number as a natural number greater than 1 that has no positive divisors other than 1 and itself.
"""

def get_prime_numbers(numbers):
    prime_numbers = []
    for num in numbers:
        if num > 1:
            # check if num is divisible by any number between 2 and its square root
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    break
            else:
                prime_numbers.append(num)
    return prime_numbers