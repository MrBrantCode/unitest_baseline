"""
QUESTION:
Implement a function `p(t, timescale=1.)` that calculates the probability distribution function (PDF) for particle displacements over time. The function should take two parameters: `t`, representing the time, and `timescale`, a scaling factor for time units with a default value of 1. The function should return the calculated PDF value. The PDF is calculated using the formula: `(1 / sqrt(4 * pi * t)) * exp(-1 / (4 * t))`, where `t` is scaled by `timescale` before calculation.
"""

import math

def p(t, timescale=1.):
    """
    Calculate the probability distribution function (PDF) for particle displacements over time.

    Args:
    t (float): Time
    timescale (float): Scaling factor for time units (default is 1)

    Returns:
    float: The calculated PDF value
    """
    t *= timescale
    return (1 / math.sqrt(4 * math.pi * t)) * math.exp(-1 / (4 * t))