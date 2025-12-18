"""
QUESTION:
Define a function `max_first_turn_stones(n)` to calculate the sum of the maximum number of stones a player can remove from a winning position during their first turn for all numbers up to `n`, modulo 10^8. The function should not take any input other than the integer `n` and return the calculated sum.
"""

MOD = 10 ** 8

def max_first_turn_stones(n):
    a, b = 1, 2
    m = 1
    result = 0
    while m <= n:
        if a != 1:
            result = (result + (b - a - 1) // a * m) % MOD
        m, a, b = m * b, b, a + b
    return result