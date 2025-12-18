"""
QUESTION:
Determine the function `calc_p_positions` and use it to find the last 9 digits of `M(10**7 + 19, 100)`, where `M(n, c)` denotes the count of potential initial arrangements that guarantee Alice's triumph in a strategic game, given an `n` by `n` board with `c` distinct coins. Function `calc_p_positions` should take parameters `x`, `y`, `a`, and `b` and recursively calculate P-positions. It should also store the calculated P-positions in lists `a` and `b`. If `x` is less than or equal to the last element in `a` or `y` is less than or equal to the last element in `b`, the function should return without further calculations. Otherwise, it should append `x` and `y` to lists `a` and `b`, and call itself with new `x` and `y` values.
"""

def calc_p_positions(x, y, a, b):
    if x <= a[-1] or y <= b[-1]:
        return
    a.append(x)
    b.append(y)
    calc_p_positions(int(x / ((1 + 5 ** 0.5) / 2)), int(y / ((1 + 5 ** 0.5) / 2)), a, b)