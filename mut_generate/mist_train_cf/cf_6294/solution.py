"""
QUESTION:
Write a JavaScript function `sumPrimesGreaterThan1000` that accepts an array of numbers and returns the sum of all prime numbers greater than 1000 in the array. The function should not accept any other data type as input. The function should check each number in the array, filter out the non-prime numbers and numbers less than or equal to 1000, and then return the sum of the remaining prime numbers.
"""

def sum_primes_greater_than_1000(numbers):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    prime_sum = 0
    for num in numbers:
        if num > 1000 and is_prime(num):
            prime_sum += num

    return prime_sum