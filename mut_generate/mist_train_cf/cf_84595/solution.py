"""
QUESTION:
Divide two integers without using multiplication, division, and mod operator. The result should be the quotient obtained after dividing `dividend` by `divisor`, truncating towards zero. The operation should be performed within the 32-bit signed integer range `[−2^31, 2^31 − 1]`. If the division result exceeds the limit, return `2^31 − 1`. The function should handle both positive and negative numbers and determine the sign of the result based on the original numbers.

Function: `divide(dividend: int, divisor: int) -> int`

Restrictions:
- `−2^31 <= dividend, divisor <= 2^31 - 1`
- `divisor != 0`
"""

def divide(dividend: int, divisor: int) -> int:
    int_max = 2**31 - 1
    int_min = -2**31
    if dividend == int_min and divisor == -1:
        return int_max
    a, b, res = abs(dividend), abs(divisor), 0
    for x in range(31, -1, -1):
        if (a >> x) - b >= 0:
            res += 1 << x
            a -= b << x
    return res if (dividend > 0) == (divisor > 0) else -res