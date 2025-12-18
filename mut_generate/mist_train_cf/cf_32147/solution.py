"""
QUESTION:
Implement a function `finite_difference_wave_equation(dx, dt, vs, x, u0, u1, t_max)` that takes in the spatial step size `dx`, time step size `dt`, wave velocity `vs`, array of spatial coordinates `x`, initial displacements `u0`, displacements at the next time step `u1`, and maximum time to simulate `t_max`. The function should return an array of arrays representing the displacements at each spatial coordinate for each time step, assuming the initial displacement at time `t = 0` is given by `u0` and the displacement at time `t = dt` is given by `u1`.
"""

import numpy as np

def finite_difference_wave_equation(dx, dt, vs, x, u0, u1, t_max):
    num_steps = int(t_max / dt)
    num_points = len(x)
    displacements = [u0, u1]

    for _ in range(2, num_steps + 1):
        u_next = np.zeros(num_points)
        for i in range(1, num_points - 1):
            u_next[i] = 2 * displacements[-1][i] - displacements[-2][i] + (vs ** 2) * (dt ** 2) / (dx ** 2) * (
                    displacements[-1][i + 1] - 2 * displacements[-1][i] + displacements[-1][i - 1])
        displacements.append(u_next)

    return displacements