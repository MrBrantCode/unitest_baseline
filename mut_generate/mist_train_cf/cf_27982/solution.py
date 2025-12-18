"""
QUESTION:
Implement a function `get_cube_lines(nx, ny, nz, coords, charges, vox_size)` that calculates cube values based on given parameters. The function should take six parameters: three integers `nx`, `ny`, `nz` representing the dimensions of the cube, a list of coordinates `coords`, a list of charges `charges`, and a voxel size `vox_size`. It should return three values: a list of cube values `cube_val_lines`, and the minimum and maximum values `min_val` and `max_val` of the cube values.
"""

import numpy as np

def get_cube_lines(nx, ny, nz, coords, charges, vox_size):
    cube_vals = np.zeros((nx, ny, nz))
    for i in range(len(coords)):
        x, y, z = coords[i]
        cube_vals[x, y, z] += charges[i]

    cube_val_lines = []
    for x in range(nx):
        for y in range(ny):
            for z in range(nz):
                cube_val_lines.append(cube_vals[x, y, z])

    min_val = min(cube_val_lines)
    max_val = max(cube_val_lines)

    return cube_val_lines, min_val, max_val