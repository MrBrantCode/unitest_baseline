"""
QUESTION:
Create a function called `generate_primes_dict` that returns a dictionary with five key-value pairs, where each key is a unique string and each value is a list of the first five prime numbers. The function should not take any arguments.
"""

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def generate_primes_dict():
    primes = []
    num = 2
    while len(primes) < 5:
        if is_prime(num):
            primes.append(num)
        num += 1
    keys = ["Key1", "Key2", "Key3", "Key4", "Key5"]
    return dict.fromkeys(keys, primes[:])