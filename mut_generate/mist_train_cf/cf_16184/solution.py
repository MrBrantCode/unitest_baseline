"""
QUESTION:
Create a function named `sum_even_prime` that takes an integer `n` as input and calculates the sum of all even numbers and prime numbers between 1 and `n` (inclusive). The function should return or print the sum of even numbers and the sum of prime numbers. The input number `n` is a positive integer greater than 1.
"""

def sum_even_prime(n):
    even_sum = 0
    prime_sum = 0

    for num in range(2, n+1):
        if num % 2 == 0:
            even_sum += num
        if all(num % i != 0 for i in range(2, int(num ** 0.5) + 1)) and num > 1:
            prime_sum += num

    return even_sum, prime_sum