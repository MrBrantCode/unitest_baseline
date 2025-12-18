"""
QUESTION:
Develop a function `select_kth_prime(lst, k)` that selects the kth prime number from the given list of natural numbers `lst`. The function should return -1 if there is no kth prime number in the list or if k is less than or equal to 0. Ensure the function is efficient and handles potential issues such as out-of-range errors and non-prime numbers, especially for large lists and large prime numbers.
"""

def select_kth_prime(lst, k):
    def is_prime(n):
        if n <= 1:
            return False
        if n == 2 or n == 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i = i + 6
        return True

    primes = [num for num in lst if is_prime(num)]
    return primes[k - 1] if 0 < k <= len(primes) else -1