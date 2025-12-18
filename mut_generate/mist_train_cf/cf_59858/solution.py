"""
QUESTION:
Write a function named `calculate_gravitational_force` that takes two parameters: `m1` (mass of an object in kg) and `r` (distance from the center of the Earth to the object in meters), and returns the intensity of gravitational influence exerted by the Earth on the object. Assume the mass of the Earth is approximately 5.972 × 10^24 kg and the gravitational constant is 6.67430 × 10^−11 m^3 kg^−1 s^−2.
"""

def calculate_gravitational_force(m1, r):
  G = 6.67430 * (10 ** -11) # gravitational constant in m^3 kg^−1 s^−2
  m2 = 5.972 * (10 ** 24) # mass of Earth in kg
  F = G * (m1 * m2) / (r ** 2) # calculate the force
  return F # return the computed value