"""
QUESTION:
Implement a function `get_fifth_prime` to retrieve the 5th prime number from a given list of numbers using a recursive approach. The function should take in a list of numbers and return the 5th prime number found in the list. If no 5th prime number exists, the function should return `None`. The input list contains a sequence of integers.
"""

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def get_fifth_prime(numbers, count=0, index=0):
    if index >= len(numbers):
        return None

    if is_prime(numbers[index]):
        count += 1

    if count == 5:
        return numbers[index]

    return get_fifth_prime(numbers, count, index + 1)