"""
QUESTION:
Create a function `add_prime_number(arr, prime_number)` that takes an array of integers `arr` and an integer `prime_number` as input. The function should add `prime_number` to every element in `arr`, but only if `prime_number` is an odd prime number. If `prime_number` is not an odd prime number, return the original array `arr`.
"""

def add_prime_number(arr, prime_number):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    if is_prime(prime_number) and prime_number % 2 == 1:
        return [num + prime_number for num in arr]
    return arr