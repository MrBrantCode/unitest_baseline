"""
QUESTION:
Write a function `count_and_sum_primes` that takes an array of integers as input, counts the number of prime numbers in the array (ignoring negative integers), and returns a tuple containing the count of prime numbers and the sum of these prime numbers. The function should consider 0 and 1 as non-prime numbers.
"""

def count_and_sum_primes(arr):
    def is_prime(num):
        if num < 2:  
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    count = 0
    prime_sum = 0
    for num in arr:
        if num >= 0 and is_prime(num):
            count += 1
            prime_sum += num
    return count, prime_sum