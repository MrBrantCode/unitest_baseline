"""
QUESTION:
Implement the function `convertToBase7(num: int) -> str` to convert an integer `num` to its base 7 representation as a string. The base 7 representation should be obtained by repeatedly dividing the number by 7 and noting down the remainders in reverse order. If `num` is negative, the base 7 representation should also be negative. The function should handle the case where `num` is 0.
"""

def convertToBase7(num: int) -> str:
    result = ''
    n = abs(num)
    while n:
        n, curr = divmod(n, 7)
        result = str(curr) + result
    return '-' * (num < 0) + result or '0'