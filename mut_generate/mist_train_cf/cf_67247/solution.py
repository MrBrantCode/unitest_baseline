"""
QUESTION:
Implement a function `rounded_avg_custom_base(n, m, base)` that takes three integers as input: `n`, `m`, and `base`. The function should calculate the average of the integers from `n` to `m` (inclusive), round it to the nearest integer, and convert it to a custom base representation. The custom base `base` should be an integer in the range [2, 10]. If `n` is greater than `m` or `base` is outside the allowed range, return -1. The custom base representation should be prefixed with "0b" for binary (base 2), "0o" for octal (base 8), and no prefix for other bases.
"""

def rounded_avg_custom_base(n, m, base):
    """You are given two positive integers n and m, and your task is to compute the
    average of the integers from n through m (including n and m). 
    Round the answer to the nearest integer and convert that to a custom base system.
    The custom base system should be another integer (base) in the range [2, 10] (inclusive).
    If n is greater than m, return -1.
    If base is outside of the allowed range, also return -1.
    """
    if n > m or base < 2 or base > 10:
        return -1

    avg = round((n + m) / 2)
    
    digits = []
    if avg == 0:
        digits.append("0")
    else:
        while avg:
            digits.append(str(avg % base))
            avg //= base
        
    custom_base_num = "".join(digits[::-1])
    
    if base == 2:
        return "0b" + custom_base_num
    elif base == 8:
        return "0o" + custom_base_num
    else:
        return custom_base_num