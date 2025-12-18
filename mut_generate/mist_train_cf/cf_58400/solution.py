"""
QUESTION:
Write a function `is_divisible(num, p)` that determines if the sum of individual digits in integer `num` raised to the power of themselves is divisible by prime number `p`. The function should have a time complexity of O(d), where d is the number of digits in the integer, and a space complexity of O(1).
"""

def is_divisible(num, p):
    """
    Determines if the sum of individual digits in integer `num` raised to the power of themselves is divisible by prime number `p`.

    Args:
        num (int): The number to check.
        p (int): The prime number.

    Returns:
        bool: True if the sum is divisible, False otherwise.
    """
    if p == 1:  # base case 1
        return False
    if num == 0:  # base case 2
        return False
    cnt = 0
    while num > 0:
        num, digit = divmod(num, 10)
        cnt += digit ** digit
    return cnt % p == 0