"""
QUESTION:
Create a function `prime_numbers` that takes a positive integer `n` as input and returns a sorted list of all prime numbers up to `n` in descending order. The function should have a time complexity of O(n^2 log n) and a space complexity of O(n).
"""

def prime_numbers(n):
    primes = []
    for num in range(n, 1, -1):
        is_prime = True
        if num > 1:
            for i in range(2, int(num**0.5) + 1):
                if num % i == 0:
                    is_prime = False
                    break
        else:
            is_prime = False
        if is_prime:
            primes.append(num)
    return primes