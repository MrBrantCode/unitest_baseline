"""
QUESTION:
Implement a function `superPow` that calculates `a` to the power of `b` modulo `1337` without using any built-in power function or the `**` operator, where `a` is a positive integer and `b` is a large positive integer represented as an array of digits. The constraints are `1 <= a <= 2^31 - 1`, `1 <= b.length <= 2000`, `0 <= b[i] <= 9`, and `b` does not contain leading zeros.
"""

def superPow(a, b):
    a %= 1337
    res = 1
    for i in range(len(b) - 1, -1, -1):
        res = (res * pow(a, b[i], 1337)) % 1337
        a = pow(a, 10, 1337)
    return res