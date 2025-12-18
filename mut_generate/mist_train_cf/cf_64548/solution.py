"""
QUESTION:
Write a function `sum_prime_indices_elements(array)` that takes an array as input and returns the sum of elements at prime indices if the length of the array is a prime number. Otherwise, return -1. A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself.
"""

def sum_prime_indices_elements(array):
    def check_prime(n):
        if n <= 1:
            return False
        elif n == 2:
            return True
        else:
            for i in range(2, int(n**0.5) + 1):
                if n % i == 0:
                    return False
            return True

    if check_prime(len(array)):
        return sum(array[i] for i in range(len(array)) if check_prime(i))
    else:
        return -1