"""
QUESTION:
Write a function `apply_rotation(dfh, symmop)` that takes a pandas DataFrame `dfh` and a 3x3 rotation matrix `symmop` as input. The DataFrame `dfh` has columns 'x', 'y', and 'z' representing the Cartesian coordinates of atoms in a crystal structure. The function should apply the rotation specified by the `symmop` matrix to the atomic positions in `dfh` and return the modified DataFrame with the rotated atomic positions. The rotation operation should be applied in place, modifying the original DataFrame.
"""

import pandas as pd
import numpy as np

def entance(dfh, symmop):
    # Convert the DataFrame to a numpy array for easier manipulation
    positions = dfh[['x', 'y', 'z']].to_numpy()

    # Apply the rotation operation to the atomic positions
    rotated_positions = np.dot(positions, symmop)

    # Update the DataFrame with the rotated atomic positions
    dfh[['x', 'y', 'z']] = rotated_positions

    return dfh