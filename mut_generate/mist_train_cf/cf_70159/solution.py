"""
QUESTION:
Create a function `circular_primes(n)` that calculates the number of circular primes below the given number `n`. A circular prime is a prime number with the property that the number generated at each intermediate step when cyclically permuting its (base 10) digits will be prime. For example, 1193 is a circular prime, since 1931, 9311 and 3119 all are also prime. The function should take an integer `n` as input and return an integer as output. It should not take any other inputs.
"""

def circular_primes(n):
    def is_prime(num):
        if num == 2 or num == 3:
            return True
        if num < 2 or num % 2 == 0:
            return False
        if num < 9:
            return True
        if num % 3 == 0:
            return False
        r = int(num ** 0.5)
        f = 5
        while f <= r:
            if num % f == 0:
                return False
            if num % (f + 2) == 0:
                return False
            f += 6
        return True

    def rotate(input_str, d):
        return input_str[d:] + input_str[:d]

    total = 0
    for num in range(2, n):
        if is_prime(num):
            str_num = str(num)
            if all(is_prime(int(rotate(str_num, d))) for d in range(len(str_num))):
                total += 1
    return total