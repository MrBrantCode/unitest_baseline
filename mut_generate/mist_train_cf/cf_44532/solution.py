"""
QUESTION:
Write a function called `power` that takes three parameters: `base`, `exp`, and `mod`, and returns the last `10` digits of `base` raised to the power of `exp` without using the built-in power function or logarithms. The function should be efficient enough to handle large `exp` values within a reasonable time frame. The function should utilize modular exponentiation to avoid calculating the entire result and instead extract the last `10` digits directly.
"""

def power(base, exp, mod):
    result = 1
    base = base % mod

    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % mod
        exp = exp >> 1
        base = (base * base) % mod

    return result