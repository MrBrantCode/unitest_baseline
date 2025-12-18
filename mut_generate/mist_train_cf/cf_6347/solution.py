"""
QUESTION:
Create a function `calculate_photon_energy(wavelength)` to calculate the energy of a photon given its wavelength in meters. The function should use Planck's constant (6.62607004e-34) and the speed of light (3.0e8). The energy should be returned in joules. However, the final answer should be provided in electron volts (eV) by dividing the energy by the conversion factor (1.60218e-19).
"""

def calculate_photon_energy(wavelength):
    plancks_constant = 6.62607004e-34
    speed_of_light = 3.0e8
    conversion_factor = 1.60218e-19
    
    frequency = speed_of_light / wavelength
    energy = plancks_constant * frequency
    
    return energy / conversion_factor