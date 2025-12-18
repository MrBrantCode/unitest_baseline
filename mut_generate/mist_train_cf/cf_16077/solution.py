"""
QUESTION:
Create a function to print all prime numbers from 1 to a given input number and calculate the sum of these prime numbers. The input number should be a positive integer greater than 1. Implement a helper function `is_prime(num)` to check if a number is prime.
"""

def entrance(num):
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    prime_numbers = [n for n in range(2, num + 1) if is_prime(n)]
    print("Prime numbers from 1 to", num, "are:")
    for prime in prime_numbers:
        print(prime)
    prime_sum = sum(prime_numbers)
    print("Sum of prime numbers from 1 to", num, "is:", prime_sum)