"""
QUESTION:
Implement a function `calculate_moving_average(data, settings)` that calculates the moving average of a given dataset. The function takes in two parameters: `data` dictionary containing a list of `datapoints` and `settings` dictionary containing an integer `periods_to_graph` specifying the number of samples to average. The function should calculate the moving average by taking the sum of `periods_to_graph` consecutive data points and dividing by `periods_to_graph` and return a list of the moving average values.
"""

def calculate_moving_average(data, settings):
    moving_averages = []
    
    for i in range(0, len(data['datapoints']) - settings['periods_to_graph'] + 1):
        average = sum(data['datapoints'][i:i + settings['periods_to_graph']]) / settings['periods_to_graph']
        moving_averages.append(average)
    
    return moving_averages