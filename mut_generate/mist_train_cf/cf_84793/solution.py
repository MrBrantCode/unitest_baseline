"""
QUESTION:
Create a function `replace_primes_with_zero` that takes a multi-dimensional array of variable depth as input, replaces all prime numbers with 0, and returns the modified array. The function should not use any built-in prime checking functions.
"""

def replace_primes_with_zero(arr):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5)+1):
            if num % i == 0:
                return False 
        return True

    for i in range(len(arr)):
        if isinstance(arr[i], list):
            replace_primes_with_zero(arr[i])
        elif is_prime(arr[i]):
            arr[i] = 0