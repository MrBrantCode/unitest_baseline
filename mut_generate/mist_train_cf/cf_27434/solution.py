"""
QUESTION:
Implement a function `calculate_equivalent_bending_moment` that takes five parameters: the alternating bending moment `M_a`, the mean bending moment `M_m`, the maximum bending moment `M_max`, the number of cycles `N_eq`, and the stress concentration factor `m`. Calculate the equivalent bending moment using the Goodman method correction, where the ultimate bending moment `M_u` is assumed to be `1.5 * M_max`. Return the sum of the equivalent bending moments for the given number of cycles.
"""

def calculate_equivalent_bending_moment(M_a, M_m, M_max, N_eq, m):
    M_u = 1.5 * M_max
    M_ar = M_a / (1 - M_m / M_u)
    return M_ar * N_eq * m