"""
QUESTION:
Calculate the pH of a solution after mixing 0.1M aqueous ammonia with excess ammonium chloride at 25°C. The function should take the initial concentration of ammonia, the dissociation constant of ammonium ion, and the temperature as input and return the pH of the solution. Assume the dissociation constant of water is not required for the calculation.
"""

import math

def calculate_pH(NH3_conc, Ka, temp):
    # Concentration of ammonia and ammonium ion at equilibrium
    x = 0.0211
    NH3_conc_eq = NH3_conc + x
    NH4_conc_eq = NH3_conc - x
    
    # pH of the solution using the Henderson-Hasselbalch equation
    pH = -math.log10(Ka) + math.log10(NH4_conc_eq / NH3_conc_eq)
    
    return pH