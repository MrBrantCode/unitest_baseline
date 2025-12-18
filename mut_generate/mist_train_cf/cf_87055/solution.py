"""
QUESTION:
Create a function called `remove_duplicates_primes` that takes an array `arr` as input. The function should return an array containing unique prime numbers from the input array, sorted in ascending order. If the input array is empty or does not contain any prime numbers, return an empty array.
"""

def remove_duplicates_primes(arr):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    result = []
    for num in arr:
        if num not in result and is_prime(num):
            result.append(num)

    return sorted(result)