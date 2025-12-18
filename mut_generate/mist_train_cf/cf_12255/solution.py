"""
QUESTION:
Write a function named `largest_prime_number` that determines the largest prime number in an unordered array of integers. The function should return the largest prime number found in the array. If no prime numbers exist in the array, the function can return None. The function should only consider integers greater than 1 as potential prime numbers.
"""

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def largest_prime_number(array):
    largest_prime = None
    for num in array:
        if is_prime(num):
            if largest_prime is None or num > largest_prime:
                largest_prime = num
    return largest_prime