"""
QUESTION:
Implement a Python function `update_position(px, py, vx, vy, ax, ay, delta_t)` that calculates the new position of a particle after a specified time interval. The function should take the initial position `(px, py)`, initial velocity `(vx, vy)`, acceleration `(ax, ay)`, and time interval `delta_t` as input, and return the new position of the particle as a tuple `(new_px, new_py)`.
"""

def update_position(px, py, vx, vy, ax, ay, delta_t):
    new_px = px + vx * delta_t + 0.5 * ax * (delta_t ** 2)
    new_py = py + vy * delta_t + 0.5 * ay * (delta_t ** 2)
    return new_px, new_py