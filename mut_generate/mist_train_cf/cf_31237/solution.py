"""
QUESTION:
Write a function `is_palindrome` that determines whether a given integer is a palindrome, which is a number that reads the same backward as forward. The function should take an integer `x` as input and return `True` if `x` is a palindrome, and `False` otherwise. The function cannot convert the integer to a string to solve this problem.
"""

def is_palindrome(x: int) -> bool:
    if x < 0 or (x % 10 == 0 and x != 0):
        return False  

    reverse_num = 0
    original_num = x

    while x > 0:
        digit = x % 10
        reverse_num = reverse_num * 10 + digit
        x = x // 10

    return original_num == reverse_num