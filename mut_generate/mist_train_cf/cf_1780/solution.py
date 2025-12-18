"""
QUESTION:
Create a function `prime_array` that generates an array of string representations of prime numbers from 0 to `n` in descending order, with no duplicates. The function should take an integer `n` as input and return the array.
"""

def prime_array(n):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    array = [str(num) for num in range(n+1) if is_prime(num)]
    array = list(set(array))
    array.sort(reverse=True)
    return array