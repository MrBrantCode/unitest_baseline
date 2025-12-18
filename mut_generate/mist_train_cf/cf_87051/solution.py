"""
QUESTION:
Generate an array of prime numbers between -100 and 100 in incremental order, excluding any prime number that ends with the digit 7. The function should be named `get_prime_numbers`. Note that the range is inclusive of -100 and exclusive of 101.
"""

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def get_prime_numbers():
    prime_numbers = []
    for i in range(-100, 101):
        if is_prime(i) and not str(i).endswith('7'):
            prime_numbers.append(i)
    return prime_numbers