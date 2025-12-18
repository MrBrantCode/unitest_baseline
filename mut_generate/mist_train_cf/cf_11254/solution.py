"""
QUESTION:
Implement a function `sum_of_primes(n)` that calculates the sum of all prime numbers up to a given integer `n`. The function should not use external libraries or built-in functions to check for prime numbers and should have a time complexity of O(n log(log n)). If `n` is less than 2, the function should output "No prime numbers up to `n`". Otherwise, the function should output the sum of prime numbers up to `n` in a human-readable format.
"""

def entrance(n):
    def is_prime(num):
        if num <= 1:
            return False
        if num <= 3:
            return True
        if num % 2 == 0 or num % 3 == 0:
            return False
        i = 5
        while i * i <= num:
            if num % i == 0 or num % (i + 2) == 0:
                return False
            i += 6
        return True

    if n < 2:
        return "No prime numbers up to " + str(n)
    prime_sum = 2
    for num in range(3, n + 1, 2):
        if is_prime(num):
            prime_sum += num
    return "Sum of prime numbers up to " + str(n) + " : " + str(prime_sum)