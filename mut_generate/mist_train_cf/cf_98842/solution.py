"""
QUESTION:
Construct a rotation matrix `rot_matrix` that rotates points by 2π/3 radians counterclockwise, with the following constraints: 
- The matrix must have a determinant of 1.
- The matrix must be invertible.
- The matrix must have integer or integer-coefficient entries.

The rotation matrix should be a 2x2 matrix with the format:
```
[ a  b ]
[ c  d ]
```
"""

import numpy as np

def rotate_matrix(theta):
    return np.array([[np.cos(theta), -np.sin(theta)],
                     [np.sin(theta), np.cos(theta)]])