"""
QUESTION:
Write a function called `convert_pascals_to_psi` that takes a pressure in Pascals as input and returns the equivalent pressure in pounds per square inch. The conversion factor is 1 Pascal = 0.0001450377377 pounds per square inch.
"""

def convert_pascals_to_psi(pascals):
    conversion_factor = 0.0001450377377 
    psi = pascals * conversion_factor
    return psi