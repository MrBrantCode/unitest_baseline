"""
QUESTION:
Write a Python function `get_aberration_terms(wavelength)` that takes a wavelength (in meters) as input and returns the corresponding aberration terms. The function should use an approximated wavelength when called with an out-of-bound wavelength. The aberration terms for wavelengths within the range are available as follows: 
- 2e-6: [0.01, 0.02, 0.01]
- 3e-6: [0.015, 0.025, 0.012]
- 4e-6: [0.018, 0.03, 0.014]
- 5e-6: [0.02, 0.03, 0.015]

The function should return the aberration terms for the closest available wavelength if the input wavelength is outside the available range.
"""

def entrance(wavelength):
    available_wavelengths = [2e-6, 3e-6, 4e-6, 5e-6]  
    aberration_terms = {
        2e-6: [0.01, 0.02, 0.01],
        3e-6: [0.015, 0.025, 0.012],
        4e-6: [0.018, 0.03, 0.014],
        5e-6: [0.02, 0.03, 0.015]
    }

    if wavelength in available_wavelengths:
        return aberration_terms[wavelength]
    else:
        closest_wavelength = min(available_wavelengths, key=lambda x: abs(x - wavelength))
        return aberration_terms[closest_wavelength]