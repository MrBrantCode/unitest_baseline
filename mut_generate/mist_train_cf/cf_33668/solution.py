"""
QUESTION:
You are given a positive integer `n`. Write a function `min_operations_to_one(n)` to find the minimum number of operations required to make `n` equal to 1. The allowed operations are subtracting 1 from `n` if it's odd, or dividing `n` by 2 if it's even.
"""

def min_operations_to_one(n: int) -> int:
    operations = 0
    while n > 1:
        if n % 2 == 0:
            n //= 2
        else:
            if n == 3 or n % 4 == 1:
                n -= 1
            else:
                n += 1
        operations += 1
    return operations