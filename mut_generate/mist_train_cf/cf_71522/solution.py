"""
QUESTION:
Write a function called `determine_data_granularity` that determines the most suitable data granularity (in minutes, hours, or shifts) for predicting energy consumption in a food processing plant based on the specific goals of the analysis.

The function should consider the trade-off between data granularity, storage costs, and processing times. It should also take into account the type of decisions the analysis aims to support (strategic decisions, real-time energy management, anomaly detection, etc.) and the capabilities of the machinery and instruments involved.
"""

def determine_data_granularity(prediction_needs):
    """
    Determine the most suitable data granularity for predicting energy consumption in a food processing plant.

    Args:
    prediction_needs (str): The specific goals of the analysis. Can be 'strategic decisions', 'real-time energy management', or 'anomaly detection'.

    Returns:
    str: The recommended data granularity in minutes, hours, or shifts.
    """
    if prediction_needs == 'strategic decisions':
        return 'shifts'
    elif prediction_needs in ['real-time energy management', 'anomaly detection']:
        return 'minutes'
    else:
        return 'hours'