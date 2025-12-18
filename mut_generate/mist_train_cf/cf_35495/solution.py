"""
QUESTION:
Create a function `calculate_sediment_flux(elevation_data)` that calculates the sediment flux at each node in a river network simulation based on the provided elevation data. The function should take a 1D array of elevation data as input and return an array representing the sediment flux at each node, where the sediment flux at each node is calculated as the difference in elevation between the current node and the previous node. The function should not calculate the sediment flux for the first node.
"""

import numpy as np

def calculate_sediment_flux(elevation_data):
    # Assuming elevation_data is a 1D array representing the elevation at each node
    num_nodes = len(elevation_data)
    sediment_flux = np.zeros(num_nodes)

    for i in range(1, num_nodes):
        sediment_flux[i] = elevation_data[i] - elevation_data[i-1]

    return sediment_flux