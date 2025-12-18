"""
QUESTION:
Write a function `prime_numbers` that takes a list of integers as input and returns two values: a list of prime numbers in descending order and the sum of these prime numbers. If there are no prime numbers in the list, the function should return an empty list and 0 as the sum.
"""

def prime_numbers(list_of_numbers):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    prime_list = [num for num in list_of_numbers if is_prime(num)]
    prime_list.sort(reverse=True)
    sum_of_primes = sum(prime_list)
    return prime_list, sum_of_primes