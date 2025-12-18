"""
QUESTION:
Implement the `velocity_derivative(v)` function that calculates the derivative of velocity based on the differential equation `v' = P/(m*v) - k*v^2/m - ug` with given constants `P`, `m`, `k`, `u`, and `g`.
"""

def velocity_derivative(v, P, m, k, u, g):
    return P / (m * v) - k * v**2 / m - u * g