"""
QUESTION:
Write a function `kth_smallest_prime(lst, k)` that takes a list of integers `lst` and an integer `k` as input, and returns the kth smallest prime number in the list. The function should return `None` if there are less than `k` prime numbers in the list. Note that `k` is 1-indexed, meaning the first prime number is considered the 1st smallest prime number, not the 0th.
"""

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    i = 3
    while i * i <= n:
        if n % i:
            i += 2
        else:
            return False
    return True

def kth_smallest_prime(lst, k):
    primes = [item for item in lst if is_prime(item)]
    primes.sort() 
    if len(primes) < k:
        return None  
    return primes[k-1]  