"""
QUESTION:
Write a function `calc_average_and_outlier` that calculates the average of values for each key in the given dictionary and identifies any outlier values. The function should return a dictionary with the average of each key and another dictionary with any outlier values. The outlier is defined as the value that deviates the most from the average value and exceeds 50% of the average.
"""

def calc_average_and_outlier(data):
    """
    Calculate the average of values for each key in the given dictionary and identify any outlier values.
    
    Args:
    data (dict): A dictionary with lists of numbers as values.
    
    Returns:
    tuple: A dictionary with the average of each key and another dictionary with any outlier values.
    """
    
    # Function to calculate average
    def calc_average(num_list):
        return sum(num_list)/len(num_list)

    # Function to calculate deviation
    def calc_deviation(num_list):
        avg = calc_average(num_list)
        deviations = [abs(num - avg) for num in num_list]
        max_deviation = max(deviations)
        max_index = deviations.index(max_deviation)
        if max_deviation > (avg * 0.5):  # If the max deviation is greater than 50% of the average, classify as an outlier
            return num_list[max_index]
        else:
            return None

    # Store averages of each key
    averages = {key: calc_average(val) for key, val in data.items()}
    
    # Store outliers of each key
    outliers = {key: calc_deviation(val) for key, val in data.items()}
    
    return averages, outliers