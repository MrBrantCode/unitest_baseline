"""
QUESTION:
Create a function named `print_prime_and_binary` that takes one integer argument `n` and prints all prime numbers in the range of 2 to `n` along with their binary representation without leading zeroes. The function should be efficient in terms of time complexity.
"""

def is_prime(n):
    if n == 2 or n == 3: return True
    if n < 2 or n % 2 == 0: return False
    if n < 9: return True
    if n % 3 == 0: return False
    r = int(n ** 0.5)
    f = 5
    while f <= r:
        if n % f == 0: return False
        if n % (f + 2) == 0: return False
        f += 6
    return True


def print_prime_and_binary(n):
    for number in range(2, n + 1):
        if is_prime(number):
            print(f'{number} = {bin(number)[2:]}')