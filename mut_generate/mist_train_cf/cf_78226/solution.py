"""
QUESTION:
Write a function `reachingPoints(sx, sy, tx, ty)` that determines whether a sequence of transformations can convert the initial point `(sx, sy)` into the destination point `(tx, ty)`, where a transformation involves taking a coordinate point `(x, y)` and converting it into either `(x, x+y)` or `(x+y, y)`. The function should return a tuple where the first element is a boolean indicating whether such a sequence is feasible, and the second element is the minimum number of transformations required to reach the destination point from the initial point. If it's not possible to reach the destination point, return `-1` as the second element of the tuple. Restrictions: `sx, sy, tx, ty` are integers within the range `[1, 10^9]`.
"""

def reachingPoints(sx, sy, tx, ty):
    steps = 0
    while tx >= sx and ty >= sy:
        if tx == ty: break
        elif tx > ty:
            if ty > sy: 
                steps += (tx - sx) // ty
                tx -= ((tx - sx) // ty) * ty
            else: 
                steps += (tx - sx) // ty
                return (ty == sy and sx <= tx), steps
        else:
            if tx > sx:
                steps += (ty - sy) // tx
                ty -= ((ty - sy) // tx) * tx
            else: 
                steps += (ty - sy) // tx
                return (tx == sx and sy <= ty), steps

    return (tx == sx and ty == sy), (steps if tx == sx and ty == sy else -1)