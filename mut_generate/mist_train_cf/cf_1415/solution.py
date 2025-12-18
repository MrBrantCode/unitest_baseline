"""
QUESTION:
Write a function `prime_numbers` that takes an integer `n` as input and returns the sum and count of prime numbers up to `n`, excluding numbers divisible by 5 and 7, and also checks if `n` is a prime number. The function should use a single loop and not utilize built-in functions or libraries for prime number calculations.
"""

def prime_numbers(n):
    count = 0
    sum_primes = 0
    is_prime = True if n >= 2 else False

    for num in range(2, n+1):
        if num % 5 == 0 or num % 7 == 0:
            continue
        
        is_num_prime = True
        for i in range(2, int(num/2)+1):
            if num % i == 0:
                is_num_prime = False
                break

        if is_num_prime:
            count += 1
            sum_primes += num

    for i in range(2, int(n/2)+1):
        if n % i == 0:
            is_prime = False
            break

    return sum_primes, count, is_prime