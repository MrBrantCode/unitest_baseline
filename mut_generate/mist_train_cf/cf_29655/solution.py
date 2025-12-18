"""
QUESTION:
Create a function `calculate_curvature` that calculates the curvature of a line in 3D space given its directional derivatives and directional components. The function accepts the following parameters:

- `ddlsfx`, `ddlsfy`, `ddlsfz` (float, optional): Directional derivatives of the line.
- `dlsfx`, `dlsfy`, `dlsfz` (float): Directional components of the line.

The function should return the curvature of the line if directional derivatives are provided, otherwise, it should return the line.
"""

import numpy as np

def calculate_curvature(ddlsfx, ddlsfy, ddlsfz, dlsfx, dlsfy, dlsfz):
    if ddlsfx is not None and ddlsfy is not None and ddlsfz is not None:
        c1xc2_1 = ddlsfz * dlsfy - ddlsfy * dlsfz
        c1xc2_2 = ddlsfx * dlsfz - ddlsfz * dlsfx
        c1xc2_3 = ddlsfy * dlsfx - ddlsfx * dlsfy

        curvature = np.sqrt(c1xc2_1 ** 2 + c1xc2_2 ** 2 + c1xc2_3 ** 2) / (dlsfx ** 2 + dlsfy ** 2 + dlsfz ** 2) ** 1.5

        return curvature
    else:
        return "Line"