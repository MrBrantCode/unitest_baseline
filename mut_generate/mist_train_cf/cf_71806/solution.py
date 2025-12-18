"""
QUESTION:
Create a function named `max_prime` that takes an integer `n` as input and returns its most significant prime divisor. The function should handle the case where `n` is itself a prime number, in which case the most significant prime divisor is `n` if `n` is greater than 2, otherwise 1 if `n` is 2. The function should not use any external libraries or complex data structures, and should be as efficient as possible.
"""

def max_prime(n):
    num = n
    max_prime = -1

    while num % 2 == 0:
        max_prime = 2
        num = num / 2

    while num % 3 == 0:
        max_prime = 3
        num = num / 3

    i = 5
    while i * i <= num:
        while num % i == 0:
            max_prime = i
            num = num / i
        while num % (i + 2) == 0:
            max_prime = i + 2
            num = num / (i + 2)
        i += 6

    if num > 4:
        max_prime = num

    return int(max_prime)