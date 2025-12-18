"""
QUESTION:
Create a function `nth_prime_greater_than_100` that takes a positive integer `n` as input and returns the nth prime number greater than 100. The function should have a time complexity of less than O(n^2).
"""

def nth_prime_greater_than_100(n):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    count = 0
    num = 101
    while count < n:
        if is_prime(num):
            count += 1
        num += 1
    return num - 1