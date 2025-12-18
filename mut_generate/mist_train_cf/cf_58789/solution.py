"""
QUESTION:
Write a function `advanced_operation(n, m, p, q)` that takes four positive integers `n`, `m`, `p`, and `q` as input and returns the total count of `n-digit` and `m-digit` positive integers that start or end with 1 and are divisible by four distinct prime numbers, plus the sum of `p-digit` and `q-digit` positive integers that start or end with 1 and are divisible by `p` and `q` respectively, if `n` and `m` are perfect squares and `p` and `q` are perfect cubes. If `n`, `m`, `p`, or `q` do not meet these criteria, or if `n` or `m` do not have at least four distinct prime divisors, return 'Invalid Inputs.'
"""

import math

def advanced_operation(n, m, p, q):
    def is_perfect_square(num):
        return math.isqrt(num) ** 2 == num

    def is_perfect_cube(num):
        return round(num ** (1. / 3)) ** 3 == num

    def is_prime(num):
        if num < 2 or num % 1 > 0:
            return False
        for i in range(2, int(math.sqrt(num)) + 1, 1):
            if num % i == 0:
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
        return divs

    if not (is_perfect_square(n) and is_perfect_square(m) and is_perfect_cube(p) and is_perfect_cube(q)):
        return 'Invalid Inputs.'
    
    n_m_prime_nums = []
    for num in [n, m]:
        if len(find_prime_divisors(num)) < 4:
            return 'Invalid Inputs.'
        else:
            n_m_prime_nums.append(find_start_end_with_one(len(str(num)), num)[0])

    p_q_total = 0
    for num in [p, q]:
        p_q_total += find_start_end_with_one(len(str(num)), num)[1]

    return sum(n_m_prime_nums) + p_q_total