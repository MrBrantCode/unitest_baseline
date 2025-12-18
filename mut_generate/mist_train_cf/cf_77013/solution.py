"""
QUESTION:
Formulate a function named `smoothclamp` that takes four parameters: a value `x` and the range `[x_min, x_max]`, and an order `N`. The function should smoothly clamp `x` within the range `[x_min, x_max]` using the N-order Smoothstep function, and return the clamped value. If `N` equals 5, use a 5th-order Smoothstep function; otherwise, use a linear function for smoothing.
"""

def smoothclamp(x, x_min, x_max, N):
    t = (x - x_min)/(x_max - x_min)
    t = np.clip(t, 0.0, 1.0)
    return x_min + (x_max - x_min) * (6*t**5 - 15*t**4 + 10*t**3) if N == 5 else x_min + (x_max - x_min) * t