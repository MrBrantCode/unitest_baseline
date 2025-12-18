"""
QUESTION:
Create a function named 'multiply_primes_by_five' that takes a list of integers as input and returns a new list where each prime number in the original list is multiplied by 5, while non-prime numbers remain unchanged. The function should not modify the original list.
"""

def multiply_primes_by_five(numbers):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    return [num * 5 if is_prime(num) else num for num in numbers]