"""
QUESTION:
Given a radioactive isotope with an initial mass of 50 grams, calculate the number of days it would take for its mass to reduce to 20 grams, given that 45 grams remain after 9 days. The solution should be rounded to the nearest day and should use the exponential decay model, where the mass at time t is given by N = N0 * e^(-λt).
"""

import math

def radioactive_decay(N0, N, t, N_final):
    """
    Calculate the time it would take for a radioactive isotope to decay from its initial mass (N0) to a final mass (N_final), 
    given that it decays from N0 to N in t days.

    Args:
        N0 (float): The initial mass of the isotope.
        N (float): The mass of the isotope after t days.
        t (float): The time elapsed in days.
        N_final (float): The final mass of the isotope we want.

    Returns:
        int: The time it would take to reduce to N_final grams, rounded to the nearest day.
    """
    # calculate decay constant
    decay_constant = -math.log(N/N0) / t

    # calculate the time it would take to reduce to N_final grams
    t_final = -math.log(N_final/N0) / decay_constant

    return round(t_final)