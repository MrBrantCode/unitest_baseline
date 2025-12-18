"""
QUESTION:
Implement a function `rounded_avg_custom_base(n, m, base)` that calculates the weighted average of the integers from `n` to `m` (inclusive), where the weight of each integer is its divisor count, rounds the average to the nearest integer, uses this value to compute the sum of an arithmetic series up to the rounded average, and converts the sum to a base `base` (between 2 and 10 inclusive). If `n` is greater than `m` or `base` is outside the allowed range, return -1.
"""

def count_divisors(n):
    count = 1 if n > 1 else 0
    d = 2
    while d * d <= n:
        if (n % d) == 0:
            if (n // d) == d:
                count += 1
            else:
                count += 2
        d += 1
    return count

def convert_to_base(num, base):
    if num == 0:
        return "0"
    nums = []
    while num:
        num, rem = divmod(num, base)
        nums.insert(0, str(rem))
    return '0' + 'b' + ''.join(nums) if base == 2 else '0' + 'o' + ''.join(nums) if base == 8 else ''.join(nums)

def rounded_avg_custom_base(n, m, base):
    if n > m or base < 2 or base > 10:
        return -1
    sum_val = 0
    weights = 0
    for i in range(n, m+1):
        weight = count_divisors(i)
        sum_val += i * weight
        weights += weight
    avg = round(sum_val / weights)
    series_sum = ((avg*(avg+1))//2)
    base_val = convert_to_base(series_sum, base)
    return base_val