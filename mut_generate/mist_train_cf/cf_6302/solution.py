"""
QUESTION:
Write a function `prime_check` that takes a positive integer `n` as input and returns the following information: 
- Whether `n` is a prime number
- The smallest prime number greater than `n`
- The sum of all prime numbers smaller than `n`

The function should not use any external libraries or pre-built functions for calculating prime numbers. It should use an efficient algorithm for checking if a number is prime and for calculating the sum of prime numbers (e.g., Sieve of Eratosthenes). The function should handle large input numbers efficiently and return the results in a well-formatted manner.
"""

def prime_check(n):
    def is_prime(num):
        if num <= 1:
            return False
        if num == 2:
            return True
        if num % 2 == 0:
            return False
        i = 3
        while i * i <= num:
            if num % i == 0:
                return False
            i += 2
        return True

    def find_smallest_prime(num):
        num += 1
        while True:
            if is_prime(num):
                return num
            num += 1

    def sum_of_primes(num):
        primes_sum = 0
        for i in range(2, num):
            if is_prime(i):
                primes_sum += i
        return primes_sum

    prime = is_prime(n)
    smallest_prime = find_smallest_prime(n)
    sum_primes = sum_of_primes(n)
    
    return {
        "is_prime": prime,
        "smallest_prime_greater_than_n": smallest_prime,
        "sum_of_primes_smaller_than_n": sum_primes
    }