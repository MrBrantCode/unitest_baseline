"""
QUESTION:
Define a function `advanced_operation(n, m, p, q)` that takes four integers as input. The function should first check if `m` is a perfect cube and both `p` and `q` are perfect cubes. Then, for `n` and `m`, check if each has at least four prime divisors. If any of these conditions are not met, return 'Invalid Inputs.' Otherwise, for `n` and `m`, find the count of numbers that start or end with 1 and are divisible by `n` or `m` respectively, within the range from `10^(number of digits in n or m - 1)` to `10^(number of digits in n or m) - 1`, and return the sum of these counts plus the sum of all numbers that start or end with 1 and are divisible by `p` or `q` respectively, within the same range.

Restrictions: 
- The function should return 'Invalid Inputs.' if `m` is not a perfect cube or if `p` and `q` are not perfect cubes.
- The function should return 'Invalid Inputs.' if `n` or `m` has less than four prime divisors.
"""

import math

def is_perfect_cube(n):
    return round(n**(1./3))**3 == n

def is_prime(n):
    if n < 2 or n % 1 > 0:
        return False
    for i in range(2, int(math.sqrt(n)) + 1, 1):
        if n % i == 0:
            return False
    return True

def find_start_end_with_one(num_digits, divisor):
    lower = 10 ** (num_digits - 1)
    upper = 10 ** num_digits - 1

    if upper < lower:
        return -1

    cnt = 0
    total = 0
    for num in range(lower, upper + 1):
        if str(num)[0] == '1' or str(num)[-1] == '1':
            if num % divisor == 0:
                cnt += 1
                total += num
    return cnt, total

def find_prime_divisors(num):
    divs = set()
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            if is_prime(i):
                divs.add(i)
            if is_prime(num // i):
                divs.add(num // i)
    if is_prime(num):
        divs.add(num)
    return divs

def advanced_operation(n, m, p, q):
    if not (is_perfect_cube(m) and is_perfect_cube(p) and is_perfect_cube(q)):
        return 'Invalid Inputs.'

    if len(find_prime_divisors(n)) < 4 or len(find_prime_divisors(m)) < 4:
        return 'Invalid Inputs.'

    n_m_prime_nums = 0
    for num in [n, m]:
        n_m_prime_nums += find_start_end_with_one(len(str(num)), num)[0]

    p_q_total = 0
    for num in [p, q]:
        p_q_total += find_start_end_with_one(len(str(num)), num)[1]

    return n_m_prime_nums + p_q_total