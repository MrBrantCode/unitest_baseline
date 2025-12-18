"""
QUESTION:
Implement the function `calculate_influence_coefficient_matrix` to calculate the influence coefficient matrix for a potential flow problem in fluid mechanics. The function takes two input lists: `z_col` containing the z-coordinates of collocation points and `norm_vec` containing the normal vectors at these collocation points. It should return the influence coefficient matrix A as a 2D list, where A[i][j] represents the influence of the j-th singularity on the velocity potential at the i-th collocation point, calculated as -1/(2*pi) * ln(r), where r is the distance between the j-th singularity and the i-th collocation point. The function should handle cases where i equals j by leaving the corresponding matrix element as zero, since the influence of a singularity on itself is not defined.
"""

import math

def calculate_influence_coefficient_matrix(z_col, norm_vec):
    N = len(z_col)
    A = [[0] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if i != j:
                dx = z_col[j].real - z_col[i].real
                dy = z_col[j].imag - z_col[i].imag
                r = math.sqrt(dx**2 + dy**2)
                A[i][j] = -1/(2*math.pi) * math.log(r)

    return A