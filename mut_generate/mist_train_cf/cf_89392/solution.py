"""
QUESTION:
Write a function `calculate_photon_energy(wavelength)` that calculates the energy of a photon in electron volts (eV) given its wavelength in meters. Planck's constant is 6.62607004e-34 J s, and the speed of light is 3.0e8 m/s. Divide the energy by 1.60218e-19 J/eV to convert joules to electron volts. The input wavelength will be in meters.
"""

def calculate_photon_energy(wavelength):
    plancks_constant = 6.62607004e-34
    speed_of_light = 3.0e8
    conversion_factor = 1.60218e-19
    
    frequency = speed_of_light / wavelength
    energy = plancks_constant * frequency
    
    return energy / conversion_factor