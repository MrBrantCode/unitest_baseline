"""
QUESTION:
Write a Python function `is_prime_and_mersenne(n)` that takes an integer `n` as input and checks if it is a prime number and a Mersenne prime. A Mersenne prime is a prime number that is one less than a power of two. Use only base Python and do not import any libraries. The function should return a string indicating whether the number is a Mersenne prime, a prime but not a Mersenne prime, or not a prime number.
"""

def is_prime_and_mersenne(n):
    def is_prime(num):
        if num <= 1:
            return False
        elif num == 2:
            return True
        elif num % 2 == 0:
            return False
        else:
            for i in range(3, int(num**0.5)+1, 2):
                if num % i == 0:
                    return False
            return True

    def is_mersenne(num):
        i = 1
        while True:
            m = 2**i - 1
            if m == num:
                return True
            elif m > num:
                return False
            i += 1

    if is_prime(n):
        if is_mersenne(n):
            return f'{n} is a Mersenne prime'
        else:
            return f'{n} is a prime but not a Mersenne prime'
    else:
        return f'{n} is not a prime number'