"""
QUESTION:
Create a function `three_dim_weighted_mean(n, m, base, p, q, r)` that calculates a three-dimensional weighted average of a series of integral values from `n` to `m` (inclusive) and translates the result into a specified numerical system with base `base`. The weights are calculated as the product of `p`, `q`, and `r`. The function should return `-1` if the input values do not fall within the following ranges: `1 <= n <= m`, `2 <= base <= 36`, and `1 <= p <= q <= r <= m-n+1`.
"""

def three_dim_weighted_mean(n, m, base, p, q, r):
    if not 1 <= n <= m or not 2 <= base <= 36 or not 1 <= p <= q <= r <= m-n+1:
        return -1
    weights = [x * p * q * r for x in range(n, m + 1)]
    weighted_mean = round(sum(weights) / len(weights))
    alphabet = '0123456789abcdefghijklmnopqrstuvwxyz'
    base_n = []
    while weighted_mean:
        weighted_mean, rem = divmod(weighted_mean, base)
        base_n.append(alphabet[rem])
    return ''.join(reversed(base_n))