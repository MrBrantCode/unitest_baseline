"""
QUESTION:
You are given a 2D grid with minimum and maximum x and y values in `xbnds` and `ybnds`, and a number of grid points in the x and y directions in `Ns`. A discretized distribution `dist` is computed for each grid point using a probability density function. Write a function `calculate_probability(region)` that takes a rectangular region specified by its minimum and maximum x and y values and returns the probability of a random event occurring within that region according to the discretized distribution.

The function should take a list `region` of length 4, where the elements represent the minimum x, maximum x, minimum y, and maximum y values of the region, in that order. The function should return the probability of the event occurring within the specified region.
"""

def entance(region, xbnds, ybnds, Ns, dens):
    """
    Calculate the probability of a random event occurring within a specified region on a 2D grid.

    Args:
        region (list): A list of length 4, where the elements represent the minimum x, maximum x, minimum y, and maximum y values of the region, in that order.
        xbnds (list): A list containing the minimum and maximum x values of the grid.
        ybnds (list): A list containing the minimum and maximum y values of the grid.
        Ns (list): A list containing the number of grid points in the x and y directions.
        dens (2D array): A discretized distribution computed for each grid point.

    Returns:
        float: The probability of the event occurring within the specified region.
    """

    # Extract region boundaries
    xmin, xmax, ymin, ymax = region
    
    # Get the grid step sizes
    dx = (xbnds[1] - xbnds[0]) / Ns[0]
    dy = (ybnds[1] - ybnds[0]) / Ns[1]
    
    # Initialize probability sum
    probability_sum = 0.0
    
    # Iterate over grid points
    for i in range(Ns[0]):
        for j in range(Ns[1]):
            # Calculate the coordinates of the grid point
            x = xbnds[0] + i * dx + dx / 2
            y = ybnds[0] + j * dy + dy / 2
            
            # Check if the grid point is within the specified region
            if xmin <= x <= xmax and ymin <= y <= ymax:
                # Add the probability at this grid point to the sum
                probability_sum += dens[i, j]
    
    # Calculate the total probability within the region
    total_probability = probability_sum * dx * dy
    
    return total_probability