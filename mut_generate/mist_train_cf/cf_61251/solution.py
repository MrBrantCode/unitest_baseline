"""
QUESTION:
Write a function named `five_in_prime` that takes an integer `n` as input. The function should calculate the number of times the digit 5 appears in prime numbers less than `n`. A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself.
"""

def five_in_prime(n: int) -> int:
    def is_prime(num: int) -> bool:
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    count = 0
    for i in range(2, n):
        if is_prime(i):
            count += str(i).count('5')
    return count