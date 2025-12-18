"""
QUESTION:
Create a function named find_smallest_prime(n) that finds the smallest prime number greater than the given input number n. The function should not take any additional arguments other than n. The input number n can be any integer, and the function should return the smallest prime number greater than n.
"""

def find_smallest_prime(n):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    num = n + 1
    while True:
        if is_prime(num):
            return num
        num += 1