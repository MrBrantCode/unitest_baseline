"""
QUESTION:
Write a function `find_prime_numbers(numbers, target)` that takes a list of numbers and a target sum as input and returns the first pair of prime numbers in the list that add up to the target sum. The function should return an empty list if no such pair exists. Assume the input list only contains integers and the target sum is a positive integer.
"""

def find_prime_numbers(numbers, target):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    primes = []
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            if numbers[i] + numbers[j] == target and is_prime(numbers[i]) and is_prime(numbers[j]):
                return [numbers[i], numbers[j]]
    return []