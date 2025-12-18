"""
QUESTION:
Write a function `bulbSwitch(n)` that takes an integer `n` as input, where `n` is the number of bulbs. The function should return the number of bulbs that are on after `n` rounds of toggling, where in each round `i`, every `i`th bulb is toggled, and in every `m`th round where `m` is a prime number, all bulbs are toggled. The input `n` is guaranteed to be in the range `0 <= n <= 10^9`.
"""

def bulbSwitch(n: int) -> int:
    import math
    if n <= 0: return 0
    x = int(math.sqrt(n))
    return 0 if x*x<n else x