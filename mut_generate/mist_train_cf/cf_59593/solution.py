"""
QUESTION:
Create a function `optimal_trajectory` that generalizes multiple vehicle trajectories from point A to point B into a single optimal trajectory with the least energy consumption. The function should take in time-series coordinate data and energy consumption data as input.
"""

def optimal_trajectory(time_series_data, energy_consumption_data):
    """
    This function takes in time-series coordinate data and energy consumption data 
    and returns the optimal trajectory with the least energy consumption.

    Parameters:
    time_series_data (list): A list of time-series coordinate data.
    energy_consumption_data (list): A list of energy consumption data.

    Returns:
    list: The optimal trajectory with the least energy consumption.
    """
    
    # Initialize a 2D table to store the minimum energy consumption for each sub-path.
    # The table will have (len(time_series_data) + 1) rows and (len(energy_consumption_data) + 1) columns.
    dp_table = [[0] * (len(energy_consumption_data) + 1) for _ in range(len(time_series_data) + 1)]
    
    # Initialize the base case where there is only one point in the time-series data.
    for i in range(len(time_series_data) + 1):
        dp_table[i][0] = 0
    
    # Initialize the base case where there is only one point in the energy consumption data.
    for j in range(len(energy_consumption_data) + 1):
        dp_table[0][j] = 0
    
    # Fill up the table using dynamic programming.
    for i in range(1, len(time_series_data) + 1):
        for j in range(1, len(energy_consumption_data) + 1):
            # Calculate the minimum energy consumption for the current sub-path.
            dp_table[i][j] = min(dp_table[i-1][j-1] + energy_consumption_data[j-1], dp_table[i-1][j] + energy_consumption_data[j-1])
    
    # Backtrack to find the optimal trajectory.
    optimal_trajectory = []
    i, j = len(time_series_data), len(energy_consumption_data)
    while i > 0 and j > 0:
        if dp_table[i][j] == dp_table[i-1][j-1] + energy_consumption_data[j-1]:
            optimal_trajectory.append(time_series_data[i-1])
            i -= 1
            j -= 1
        else:
            i -= 1
    
    # Return the optimal trajectory in the correct order.
    return optimal_trajectory[::-1]