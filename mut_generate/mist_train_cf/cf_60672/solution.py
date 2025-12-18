"""
QUESTION:
Write a function `calculate_sum` that takes an integer `upper_limit` and an integer `power` as input, and returns the sum of the expected values of `g(n)` for all `n` from 2 to `upper_limit`, where `g(n)` is the expected value of the smallest index `k` such that the sequence `p_k, p_{k + 1}, ..., p_{k + d - 1}` matches the decimal digits of `n`, and `d` is the number of decimal digits in `n`. The sequence `p` is an infinite sequence of random digits chosen from the set `{0,1,2,3,4,5,6,7,8,9}` with equal likelihood.

The function should use the fact that `g(n) = 10^d`, where `d` is the number of decimal digits in `n`. The function should also use the fact that `n` is calculated as `floor(10^power / k)`.

Restriction: The input `upper_limit` and `power` are positive integers, and `upper_limit` is less than or equal to `10^6` and `power` is less than or equal to 16.
"""

def calculate_sum(upper_limit: int, power: int) -> int:
    sum_ = 0
    for n in range(2, upper_limit + 1):
        d = len(str(pow(10, power) // n))
        sum_ += pow(10, d)

    return sum_