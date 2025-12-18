"""
QUESTION:
Write a function `convert_all_sums(n, m, start, base)` that takes four parameters: two positive integers `n` and `m` where `n <= m`, an additional starting number `start`, and a custom base system `base` ranging from 2 to 10 inclusive. The function should calculate the sum of all numbers from `n` through `m` (inclusive), add the `start` number, and then convert the sum into the custom base system. If `n` is greater than `m`, the `start` number is less than zero, or the `base` is out of the given range, the function should return -1.
"""

def convert_all_sums(n, m, start, base):
    """
    You are provided two positive integers n and m (n <= m), 
    and an additional starting number (start), 
    your task is to determine the sum of all the numbers from n through m (inclusive), starting from the 'start' number,
    Then convert the sum into a custom base system. The custom base system will be another integer (base)
    ranging from [2, 10] (inclusive), If n is greater than m, the start number is less than zero,
    or the base is out of the given range, return -1.
    """
    # Check for valid input
    if n > m or start < 0 or not(2 <= base <= 10):
        return -1
    # Calculates the sum of the series
    total = sum(range(n, m+1)) + start
    # Converts the sum to the appropriate base
    if base == 2:
        return bin(total)
    elif base == 8:
        return oct(total)
    elif base == 10:
        return str(total)
    else:
        digits = []
        while total:
            digits.append(int(total % base))
            total //= base
        return ''.join(map(str, digits[::-1]))