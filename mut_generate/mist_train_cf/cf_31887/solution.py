"""
QUESTION:
Implement the function `construct_mesh_grid(vinf_span, alpha_lim, num_contours, N, V_body)` that takes in the following inputs: 
- `vinf_span`: A list representing the range of free-stream velocities 
- `alpha_lim`: A list representing the range of angles of attack 
- `num_contours`: An integer representing the number of contours for free-stream velocity 
- `N`: An integer representing the number of points for angle of attack 
- `V_body`: A float representing the body velocity 

The function should construct a mesh grid for any configuration using the provided inputs and return the mesh grid as two 2D arrays: `V_INF` and `ALPHA`.
"""

import numpy as np

def entance(vinf_span, alpha_lim, num_contours, N, V_body):
    vinf_array = np.linspace(vinf_span[0], vinf_span[-1], num_contours)
    alpha_array = np.linspace(alpha_lim[0], alpha_lim[-1], N)
    vinf_array /= V_body
    V_INF, ALPHA = np.meshgrid(vinf_array, alpha_array)
    return V_INF, ALPHA