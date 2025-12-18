"""
QUESTION:
Implement a function `delete_primes(arr, n)` that takes an array of integers `arr` and a number `n` as input, and returns the modified array with all prime numbers from the first `n` numbers removed. The function should not use any built-in functions or libraries to check for prime numbers and should handle edge cases such as when `n` is less than or equal to 0 or when the array is empty.
"""

def delete_primes(arr, n):
    if n <= 0 or len(arr) == 0:
        return arr

    def is_prime(num):
        if num <= 1:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    primes = [num for num in arr[:n] if is_prime(num)]
    return [num for num in arr if num not in primes]