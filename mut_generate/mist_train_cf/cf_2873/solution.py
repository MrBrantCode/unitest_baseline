"""
QUESTION:
Write a function `get_sum_of_primes` that calculates the sum of the first 100 prime numbers, excluding any prime numbers that end with the digit 7 and are palindromes. The function should return the calculated sum.
"""

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def get_sum_of_primes():
    count = 0
    prime_sum = 0
    current_number = 2

    while count < 100:
        if current_number % 10 == 7 and str(current_number) == str(current_number)[::-1]:
            current_number += 1
            continue

        if is_prime(current_number):
            prime_sum += current_number
            count += 1

        current_number += 1

    return prime_sum