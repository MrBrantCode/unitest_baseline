"""
QUESTION:
Design a function named `rounded_avg_custom_base` that takes three parameters: two positive integers `n` and `m` (where `n` is less than or equal to `m`), and an integer `base` between 2 and 10 (inclusive). The function should compute the weighted average of the integers from `n` through `m` (including `n` and `m`), with weights given by their divisors' count, round the average to the nearest integer, and convert that to a custom base system represented by the `base` parameter. If `n` is greater than `m` or `base` is outside of the allowed range, return -1.
"""

def rounded_avg_custom_base(n, m, base):
    if n > m or base < 2 or base > 10:
        return -1

    div_counts = [len([i for i in range(1, num + 1) if num % i == 0]) for num in range(n, m + 1)]
    weighted_avg = round(sum([count * num for count, num in zip(div_counts, range(n, m + 1))]) / sum(div_counts))

    if base < 2 or base > 10:
        return -1

    digits = []
    while weighted_avg > 0:
        digits.append(str(weighted_avg % base))
        weighted_avg //= base

    if base == 2:
        prefix = "0b"
    elif base == 8:
        prefix = "0o"
    else:
        prefix = ""

    return "{}{}".format(prefix, "".join(digits[::-1]))