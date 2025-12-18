"""
QUESTION:
Write a function `find_water_volumes(N, M, P, Q)` to calculate the original amount of water in two containers given the total volume of water `N`, the amount of water removed `M` from the larger container, and the resulting ratio `P:Q` of water in the larger container to the smaller one, where `N` is a non-negative integer not exceeding `10^6`, `0 ≤ M ≤ N/2`, and `3 ≤ P, Q ≤ N/3`.
"""

def find_water_volumes(N, M, P, Q):
    # Solve the following system of linear equations:
    # x + y = N
    # P*(x-M) = Q*y
    # where x is the original amount in the larger container and y is in the smaller one.
    # After some algebraic manipulation, we can extract y as:
    y = N * Q / (P + Q)
    # And then we can find x using the remaining portion of the total volume:
    x = N - y
    # We convert each volume to an integer because the quantities are discrete.
    # Since we are guaranteed a solution exists, this will not introduce rounding error.
    return int(x), int(y)