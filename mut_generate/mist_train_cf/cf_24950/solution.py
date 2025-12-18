"""
QUESTION:
Write a function `find_nth_prime` to find the nth prime number. The function should take one argument, `n`, which is the position of the prime number to find. The function should return the nth prime number.
"""

def find_nth_prime(n):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    count = 0
    num = 2
    while True:
        if is_prime(num):
            count += 1
            if count == n:
                return num
        num += 1