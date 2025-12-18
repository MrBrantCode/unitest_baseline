"""
QUESTION:
A number `n` is called `prime happy` if there is at least one prime less than `n` and the `sum of all primes less than n` is evenly divisible by `n`. Write `isPrimeHappy(n)` which returns `true` if `n` is `prime happy` else `false`.
"""

def is_prime_happy(n):
    if n <= 2:
        return False
    
    def is_prime(num):
        if num <= 1:
            return False
        if num <= 3:
            return True
        if num % 2 == 0 or num % 3 == 0:
            return False
        i = 5
        while i * i <= num:
            if num % i == 0 or num % (i + 2) == 0:
                return False
            i += 6
        return True
    
    prime_sum = 0
    for i in range(2, n):
        if is_prime(i):
            prime_sum += i
    
    return prime_sum % n == 0