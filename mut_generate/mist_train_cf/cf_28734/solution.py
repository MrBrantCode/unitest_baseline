"""
QUESTION:
Implement the `load_driver_aggmat_celery(driver_id, sim_groups, driver_trips_id, trips_id)` function, which takes a driver ID, a list of similarity groups `sim_groups`, a list of driver trip IDs `driver_trips_id`, and a list of trip IDs `trips_id` as input. The function should return a 2D array (aggregated matrix) containing the driver ID, driver trip IDs, trip IDs, similarity trips, and their group lengths. The function should process the similarity groups to calculate the similarity trips and their group lengths, and then create the aggregated matrix with the specified columns. The order of the columns in the aggregated matrix should be: driver ID, driver trip IDs, trip IDs, similarity trips, and their group lengths. The driver ID column should be filled with the input driver ID, and the similarity trips and their group lengths should be calculated based on the `sim_groups` list. The length of the aggregated matrix should be equal to the length of the `driver_trips_id` list, which is assumed to be 200.
"""

import numpy as np

def load_driver_aggmat_celery(driver_id, sim_groups, driver_trips_id, trips_id):
    sim_trips = {}  # Initialize dictionary to store similarity trips
    sim_trips_group = {}  # Initialize dictionary to store similarity trip group lengths

    for group in sim_groups:
        gl = len(group)  # Calculate the length of the current group
        for gid in group:
            sim_trips[gid] = 1  # Set the similarity trip entry to 1 for the current trip ID
            sim_trips_group[gid] = gl  # Store the group length for the current trip ID

    total_sim_trips = np.sum(list(sim_trips.values()))  # Calculate the total number of similarity trips for the driver

    # Create the aggregated matrix containing driver ID, driver trip IDs, trip IDs, similarity trips, and their group lengths
    res = np.c_[np.ones(len(driver_trips_id)) * int(driver_id), 
                driver_trips_id, 
                trips_id, 
                [sim_trips.get(tid, 0) for tid in trips_id], 
                [sim_trips_group.get(tid, 0) for tid in trips_id]]

    return res  # Return the aggregated matrix