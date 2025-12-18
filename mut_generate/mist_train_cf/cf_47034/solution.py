"""
QUESTION:
Write a function `generate_prime_fibonacci` that generates all Prime Fibonacci numbers within a given range. The function should take two parameters `n` and `m`, where `n` is the lower bound (greater than or equal to 100) and `m` is the upper bound (less than or equal to 1500) of the range. The function should return a list of all Prime Fibonacci numbers within the given range.
"""

def generate_prime_fibonacci(n, m):
    def check_prime(num):
        if num == 1:
            return False
        elif num == 2:
            return True
        else:
            for x in range(2, num):
                if num % x == 0:
                    return False
            return True

    seq = [0, 1]
    while seq[-1] <= m:
        seq.append(seq[-1] + seq[-2])
    
    primes = [num for num in seq if num >= n and check_prime(num)]
    return primes