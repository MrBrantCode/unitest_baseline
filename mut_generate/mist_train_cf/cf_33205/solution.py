"""
QUESTION:
Write a function `optimize_sunlight_allocation` that takes the following inputs: 
- `bed_sun_req`: An array containing the sunlight requirements for each bed
- `num_years`: The number of years over which sunlight allocation needs to be optimized

The function should return a 2D array where the number of rows is equal to the number of beds and the number of columns is equal to `num_years`, representing the optimal allocation of sunlight to each bed over the specified years. The function should ensure that each bed's sunlight requirements are met while considering the time dimension, and the allocation should be as efficient as possible.
"""

import numpy as np

def optimize_sunlight_allocation(bed_sun_req, num_years):
    # Initialize an array to store the sunlight allocation for each bed over the years
    sunlight_allocation = np.zeros((len(bed_sun_req), num_years))

    # Iterate over each bed to optimize sunlight allocation
    for bed in range(len(bed_sun_req)):
        # Calculate the total sunlight requirement for the current bed
        total_sun_req = bed_sun_req[bed]

        # Distribute sunlight evenly over the years to meet the total requirement
        sunlight_per_year = total_sun_req / num_years

        # Allocate the calculated sunlight to each year for the current bed
        sunlight_allocation[bed, :] = sunlight_per_year

    return sunlight_allocation