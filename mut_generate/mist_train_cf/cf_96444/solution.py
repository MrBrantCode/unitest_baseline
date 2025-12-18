"""
QUESTION:
Create a function called `remove_primes` that takes an array of integers as input, removes all prime numbers from the array, and returns the sum of the remaining numbers. The input array can contain any integers, including negative numbers, zero, and positive numbers. The function should return 0 if the input array is empty or if all numbers in the array are prime.
"""

def remove_primes(arr):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    return sum(num for num in arr if not is_prime(num))