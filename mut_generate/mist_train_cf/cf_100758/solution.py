"""
QUESTION:
Create a function `convert_energy_output` that takes the energy output in watt-hours as input and returns the equivalent energy output in watts. Assume that one joule is equivalent to 0.00027778 watt-hours.
"""

def convert_energy_output(energy_output):
    """
    Converts energy output from watt-hours to watts.

    Args:
        energy_output (float): Energy output in watt-hours.

    Returns:
        float: Energy output in watts.
    """
    energy_output_joules = energy_output * 3600  # convert to joules
    energy_output_watts = energy_output_joules / 3600  # convert to watts
    return energy_output_watts