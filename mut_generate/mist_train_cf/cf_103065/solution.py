"""
QUESTION:
Write a function `find_first_prime(arr)` that finds the first occurrence of a prime number in a given array of numbers and returns the prime number. If no prime number is found in the array, the function should return `None`. The input array `arr` will contain only integers.
"""

def find_first_prime(arr):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    for num in arr:
        if is_prime(num):
            return num
    return None