"""
QUESTION:
Create a function `remove_prime_sort(arr)` that takes an array of integers as input, removes any element that is a prime number, and returns the remaining elements sorted in descending order. The function should not take any additional parameters besides the input array.
"""

def remove_prime_sort(arr):
    def isPrime(n):
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    return sorted([num for num in arr if not isPrime(num)], reverse=True)