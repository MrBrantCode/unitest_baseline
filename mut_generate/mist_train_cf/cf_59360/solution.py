"""
QUESTION:
Create a function named `next_prime(n)` that finds the smallest prime number larger than the given integer `n`. The function should take one integer parameter `n` and return the smallest prime number greater than `n`.
"""

def next_prime(n):
    def is_prime(num):
        if num <= 1 or (num % 2 == 0 and num > 2): 
            return False
        return all(num % i for i in range(3, int(num**0.5) + 1, 2))

    n += 1
    while not is_prime(n):
        n += 1
    return n