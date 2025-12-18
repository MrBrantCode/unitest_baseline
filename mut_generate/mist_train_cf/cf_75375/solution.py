"""
QUESTION:
Design a function `weighted_median_custom_base(n, m, base, w1, w2)` that takes five positive integers `n`, `m`, `base`, `w1`, and `w2` as input, where `n` is less than or equal to `m`, `w1` is less than or equal to `w2`, and `base` is between 2 and 16 (inclusive). The function calculates the weighted median of the integers from `n` to `m` (inclusive), with weights derived from the prime factorization of these integers, where `w1` is the sum of the cubic roots of the prime factors and `w2` is the product of the square roots. The function returns the weighted median rounded to the nearest integer, converted to the base `base`. If `n` is greater than `m`, `w1` is greater than `w2`, or `base` is not within the defined range, the function returns -1.
"""

import math
import statistics

def weighted_median_custom_base(n, m, base, w1, w2):
    if n > m or w1 > w2 or base < 2 or base > 16:
        return -1

    def primeFactors(x):
        factors = []
        while x % 2 == 0:
            factors.append(2),
            x = x / 2
        for i in range(3, int(math.sqrt(x))+1, 2):
            while x % i== 0:
                factors.append(i),
                x = x / i
        if x > 2:
            factors.append(x)
        return factors

    def compute_weights(x):
        factors = primeFactors(x)
        w1_val = sum([math.pow(y, 1/3) for y in factors])
        w2_val = math.prod([math.sqrt(y) for y in factors])
        return (w1_val, w2_val)

    def convert_to_base(x, base):
        convertString = "0123456789ABCDEF"
        if x < base:
            return convertString[x]
        else:
            return convert_to_base(x//base, base) + convertString[x%base]

    weights = [compute_weights(x) for x in range(n, m+1)]
    weighted_nums = [(x[0]*w1 + x[1]*w2) for x in weights]
    median = round(statistics.median(weighted_nums))
    return convert_to_base(median, base)