"""
QUESTION:
Write a function `calc_number_of_jumps` that calculates the minimum number of jumps of a given length required to reach or surpass a point `(d, e)` from the origin in a 2D plane. The jumps can be made in any direction but must be of the same length. The function should handle cases where the jump length is not a perfect divisor of `d` or `e`, as well as edge cases where the jump length is zero or the destination point is at the origin.
"""

def calc_number_of_jumps(jump_length, d, e):
    # check for edge cases
    if jump_length == 0 or (d == 0 and e == 0):
        return 0
    
    dx = d//jump_length if d%jump_length == 0 else d//jump_length + 1
    dy = e//jump_length if e%jump_length == 0 else e//jump_length + 1

    return max(dx, dy)