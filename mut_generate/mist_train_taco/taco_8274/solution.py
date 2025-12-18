"""
QUESTION:
Generate and return **all** possible increasing arithmetic progressions of six primes `[a, b, c, d, e, f]` between the given limits. Note: the upper and lower limits are inclusive.

An arithmetic progression is a sequence where the difference between consecutive numbers is the same, such as: 2, 4, 6, 8.

A prime number is a number that is divisible only by itself and 1 (e.g. 2, 3, 5, 7, 11)

Your solutions should be returned as lists inside a list in ascending order of the first item (if there are multiple lists with same first item, return in ascending order for the second item etc) are the e.g: `[ [a, b, c, d, e, f], [g, h, i, j, k, l] ]` where `a < g`. If there are no solutions, return an empty list: `[]`

## Examples
"""

def generate_prime_arithmetic_progressions(lower_limit, upper_limit):
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

    a_p = []
    for n in range(lower_limit | 1, upper_limit, 2):
        for gap in range(30, (upper_limit - n) // 5 + 1, 30):
            sequence = [n + i * gap for i in range(6)]
            if all(map(is_prime, sequence)):
                a_p.append(sequence)
    return a_p