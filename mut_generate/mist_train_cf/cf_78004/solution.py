"""
QUESTION:
Develop a function named `is_divisible(num, n)` that takes two integers `num` and `n` as input and returns `True` if `num` is evenly divisible by `n`, and `False` otherwise. The function should not use built-in division, modulus, or multiplication operators. Additionally, it should handle edge cases where `num` is 0 or `n` is larger than `num`.
"""

def is_divisible(num, n):
    # Edge cases
    if n == 0:
        return False 
    if num == 0 or num == n:
        return True 

    while num >= n:
        num = num - n

    # If after all subtraction num becomes zero, then it's divisible
    if num == 0:
        return True
    # If there is a residue left then it's not divisible
    return False