"""
QUESTION:
Write a function `reachingPoints(sx, sy, tx, ty)` that determines whether a sequence of transformations can be executed to convert the initial point `(sx, sy)` into the destination point `(tx, ty)`, where a single move involves taking a coordinate point `(x, y)` and converting it into either `(x, x+y)` or `(x+y, y)`. The function should return `True` if such a sequence is feasible, and `False` otherwise. The input values `sx, sy, tx, ty` are integers within the range `[1, 10^9]`.
"""

def reachingPoints(sx, sy, tx, ty):
    while sx < tx and sy < ty:
        if tx < ty:
            ty %= tx
        else:
            tx %= ty
    return sx == tx and sy <= ty and (ty - sy) % sx == 0 or \
           sy == ty and sx <= tx and (tx - sx) % sy == 0