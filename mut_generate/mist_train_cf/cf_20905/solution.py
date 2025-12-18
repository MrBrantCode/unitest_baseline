"""
QUESTION:
Create a function called `prime_numbers` that takes one argument `n` of type integer. The function should return three values: a boolean indicating whether `n` is a prime number, the smallest prime number greater than `n`, and the sum of all prime numbers smaller than `n`. A prime number is an integer greater than 1 which is not divisible by any other numbers, except for 1 and itself. The function should not take any other arguments besides `n`.
"""

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def prime_numbers(n):
    is_prime_number = is_prime(n)
    smallest_prime = n + 1
    sum_of_primes = 0
    while True:
        if is_prime(smallest_prime):
            break
        smallest_prime += 1
    for i in range(2, n):
        if is_prime(i):
            sum_of_primes += i
    return is_prime_number, smallest_prime, sum_of_primes