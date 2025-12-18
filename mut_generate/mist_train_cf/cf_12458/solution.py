"""
QUESTION:
Create a function called `find_prime_sum` that takes a list of integers as input. The function should return the first two elements in the list whose sum is a prime number. If no such pair exists, return None.
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