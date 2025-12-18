"""
QUESTION:
Write a function named `choose_model` that determines whether a deterministic or stochastic model is better suited for a given situation. The function should take two parameters: `data_quality` (a string that can be 'high', 'medium', or 'low') and `system_complexity` (a string that can be 'simple', 'medium', or 'complex'). The function should return a string that either 'Deterministic' or 'Stochastic' based on the input parameters. Assume that a deterministic model is preferred when the data quality is high and the system complexity is simple, otherwise a stochastic model is preferred.
"""

def choose_model(data_quality, system_complexity):
    """
    This function determines whether a deterministic or stochastic model is better suited for a given situation.
    
    Parameters:
    data_quality (str): The quality of the data, which can be 'high', 'medium', or 'low'.
    system_complexity (str): The complexity of the system, which can be 'simple', 'medium', or 'complex'.
    
    Returns:
    str: A string that either 'Deterministic' or 'Stochastic' based on the input parameters.
    """

    if data_quality == 'high' and system_complexity == 'simple':
        return 'Deterministic'
    else:
        return 'Stochastic'