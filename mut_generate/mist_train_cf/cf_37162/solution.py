"""
QUESTION:
Implement the `single_step` method within a class, ensuring that it correctly advances the field by a single `z`-slice and returns the updated frequency domain representation of the electromagnetic field after propagation. The method should take the current propagation distance `z_curr` and the frequency domain representation of the field `Ew` as inputs.
"""

import numpy as np

def single_step(z_curr, Ew, medium_params):
    """
    Advance field by a single z-slice

    Args:
        z_curr (float): Current propagation distance.
        Ew (numpy.ndarray): Frequency domain representation of the field at z_curr.
        medium_params (dict): Medium parameters, including 'wavelength', 'refractive_index', and 'slice_thickness'.

    Returns:
        numpy.ndarray: Frequency domain representation of the field after propagation.
    """
    # Perform field propagation simulation here
    # Example: Assuming linear propagation, the field can be advanced using a phase shift
    k = 2 * np.pi / medium_params['wavelength']  # Wave number
    phase_shift = np.exp(1j * k * medium_params['refractive_index'] * medium_params['slice_thickness'])
    Ew_propagated = Ew * phase_shift  # Apply phase shift for propagation

    return Ew_propagated