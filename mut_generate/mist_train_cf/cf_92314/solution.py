"""
QUESTION:
Create a function named `find_prime_sum` that takes a list of integers as input and returns the first two elements whose sum is a prime number. The function should return None if no such pair exists.
"""

def find_prime_sum(numbers):
    def is_prime(num):
        if num <= 1:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    for i in range(len(numbers) - 1):
        for j in range(i + 1, len(numbers)):
            if is_prime(numbers[i] + numbers[j]):
                return numbers[i], numbers[j]
    
    return None