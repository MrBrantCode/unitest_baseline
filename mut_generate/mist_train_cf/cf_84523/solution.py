"""
QUESTION:
Write a function called `nth_prime(N)` that takes an integer `N` as input and returns the Nth prime number. A prime number is a number greater than 1 that has no positive divisors other than 1 itself and the number. The function should not count 1 as a prime number.
"""

def nth_prime(N):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    count = 0
    num = 2
    while(count < N):
        if is_prime(num):
            count += 1
        num += 1
    return num - 1