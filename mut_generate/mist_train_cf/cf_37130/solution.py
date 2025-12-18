"""
QUESTION:
Implement the function `generate_surface_of_section(orbit, constant_idx)` that takes in an `orbit` object and a `constant_idx` integer, and returns a 2D array or DataFrame containing the relevant phase space coordinates for the orbit at the specified `constant_idx`. The `orbit` object has the necessary methods and attributes to extract the phase space coordinates at a given time or constant index.
"""

import numpy as np
import pandas as pd

def generate_surface_of_section(orbit, constant_idx):
    # Extract phase space coordinates at the constant index
    phase_space_coords = orbit.get_phase_space_coords_at_constant(constant_idx)

    # Create a DataFrame to store the surface of section
    surface_of_section = pd.DataFrame(phase_space_coords, columns=['x', 'y'])

    return surface_of_section