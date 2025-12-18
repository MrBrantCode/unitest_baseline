"""
QUESTION:
Implement the `solve(x)` function to reverse the digits of the input integer `x` and return the result. The function should handle negative numbers by preserving the sign, and if the reversed integer overflows the 32-bit signed integer range (-2^31 to 2^31 - 1), it should return 0.
"""

def reverse(x):
    if x == 0:
        return 0

    sign = 1 if x > 0 else -1
    x = abs(x)
    reversed_x = 0

    while x > 0:
        digit = x % 10
        reversed_x = reversed_x * 10 + digit
        x //= 10

    reversed_x *= sign

    if reversed_x < -2**31 or reversed_x > 2**31 - 1:
        return 0
    else:
        return reversed_x