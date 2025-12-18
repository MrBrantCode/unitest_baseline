"""
QUESTION:
Create a function `volcanic_eruption_forecast` that predicts the likelihood of a volcanic eruption based on a set of preliminary warning signals and indicators. The function should take three parameters: `ground_deformation`, `seismic_activity`, and `gas_emissions`, each representing the corresponding indicator value. The function should return a value between 0 and 1 representing the likelihood of an eruption.
"""

def volcanic_eruption_forecast(ground_deformation, seismic_activity, gas_emissions):
    """
    Predicts the likelihood of a volcanic eruption based on preliminary warning signals and indicators.

    Parameters:
    ground_deformation (float): The ground deformation indicator value.
    seismic_activity (float): The seismic activity indicator value.
    gas_emissions (float): The gas emissions indicator value.

    Returns:
    float: A value between 0 and 1 representing the likelihood of an eruption.
    """
    
    # Define weights for each indicator
    deformation_weight = 0.4
    seismic_weight = 0.3
    gas_weight = 0.3
    
    # Calculate the weighted sum of the indicators
    likelihood = (deformation_weight * ground_deformation + 
                  seismic_weight * seismic_activity + 
                  gas_weight * gas_emissions)
    
    # Normalize the likelihood to be between 0 and 1
    likelihood = max(0, min(1, likelihood))
    
    return likelihood