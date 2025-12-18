"""
QUESTION:
Write a function `find_proportion(numbers, prime)` that calculates the proportion of elements in the list `numbers` that are divisible by a prime number `prime`. The function should take two parameters: a list of distinct, positive integers less than 100000 and a distinct prime number less than 100. The function should handle edge cases where the input list or prime number is None, the prime number is not a prime, or the list is empty.
"""

def is_prime(n):
    if n <= 1 or (n % 2 == 0 and n > 2): 
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def entrance(numbers, prime):
    if numbers is None or prime is None:
        return 0

    if not is_prime(prime):
        return 0
    
    if len(numbers) <= 0:
        return 0

    count = 0
    for num in numbers:
        if num % prime == 0:
            count += 1
    return count / len(numbers)