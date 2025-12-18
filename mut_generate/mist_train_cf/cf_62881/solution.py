"""
QUESTION:
Write a function `nthMagicalNumber(n, a, b)` that returns the nth magical number where a magical number is a positive integer divisible by either `a` or `b` and both `a` and `b` are prime numbers. The function should return the result modulo 10^9 + 7. If either `a` or `b` is not a prime number, return -1. The function should be able to handle `n` in the range 1 to 10^9 and `a` and `b` in the range 2 to 4 * 10^4.
"""

def nthMagicalNumber(n, a, b):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5)+1):
            if num % i == 0:
                return False
        return True

    if not is_prime(a) or not is_prime(b): 
        return -1
    MOD = 10**9+7
    lcm = a*b//math.gcd(a,b)
    left, right = 2, min(a,b)*n
    while left < right:
        mid = (left + right) // 2
        if mid//a + mid//b - mid//lcm < n: 
            left = mid + 1
        else: 
            right = mid
    return right % MOD