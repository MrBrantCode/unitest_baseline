"""
QUESTION:
Create a function `calculate_energy_output` that takes the energy output in watt-hours as input and returns the energy output in watts. The function should convert the energy output from watt-hours to joules and then to watts, using the conversion factors 1 watt-hour = 3600 joules and 1 joule = 0.00027778 watt-hours.
"""

def calculate_energy_output(energy_output):
    """
    Converts energy output from watt-hours to watts.
    
    Parameters:
    energy_output (float): Energy output in watt-hours.
    
    Returns:
    float: Energy output in watts.
    """
    energy_output_joules = energy_output * 3600  # convert to joules
    energy_output_watts = energy_output_joules * 0.00027778  # convert to watts
    return energy_output_watts