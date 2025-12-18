"""
QUESTION:
Write two functions, `generate_time_series_data(G, k1, k2, k3, num_points)` and `calculate_mse(observed_data, predicted_data)`, to generate time series data and calculate the Mean Squared Error (MSE) respectively. The `generate_time_series_data` function should take parameters G, k1, k2, k3, and num_points to generate time series data, and the `calculate_mse` function should take observed and predicted data as input to compute the MSE. The generated time series data should be plotted as a line plot and the MSE values should be plotted as another line plot in a separate subplot.
"""

def generate_time_series_data(G, k1, k2, k3, num_points):
    t_set = [i for i in range(num_points)]  # Generate time values
    n_set = [G * (k1 * i + k2 * i**2 + k3 * i**3) for i in range(num_points)]  # Generate data values
    return t_set, n_set

def calculate_mse(observed_data, predicted_data):
    squared_errors = [(observed_data[i] - predicted_data[i])**2 for i in range(len(observed_data))]
    mse = sum(squared_errors) / len(observed_data)
    return mse