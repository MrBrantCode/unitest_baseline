"""
QUESTION:
Create a function `calculate_refracted_angle` that takes a dictionary containing refraction data as input. The dictionary should have keys 'wavelength', 'refraction_index', and 'angle_of_incidence' with float values representing wavelength in nanometers, refraction index of the medium, and angle of incidence in degrees respectively. The function should return the angle of refraction in degrees calculated using Snell's Law.
"""

import math

def calculate_refracted_angle(refraction_data):
    wavelength = refraction_data['wavelength']
    refraction_index = refraction_data['refraction_index']
    angle_of_incidence = math.radians(refraction_data['angle_of_incidence'])  # Convert angle to radians

    sin_theta2 = (refraction_index / 1.0) * math.sin(angle_of_incidence)  # Snell's Law: n1=1.0 (refractive index of air)
    angle_of_refraction = math.degrees(math.asin(sin_theta2))  # Calculate angle of refraction in degrees

    return angle_of_refraction