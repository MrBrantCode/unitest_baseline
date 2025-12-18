"""
QUESTION:
Given a total mass and the densities of four types of apples (1 kg/m3, 2 kg/m3, 3 kg/m3, and 4 kg/m3), write a function named `calculate_volumes` that calculates and returns the required volume of each type to attain the given total mass.
"""

def calculate_volumes(total_mass):
    """
    Calculate the volume of each type of apple required to attain the given total mass.

    Args:
        total_mass (float): The total mass required.

    Returns:
        list: A list of volumes of each type of apple.
    """
    # Define the densities of the four types of apples
    densities = [1, 2, 3, 4]

    # Initialize an empty list to store the volumes
    volumes = []

    # Iterate over each density
    for density in densities:
        # Calculate the volume by dividing the total mass by the density
        volume = total_mass / density
        
        # Round the volume to the nearest hundredth
        volume = round(volume, 2)
        
        # Append the volume to the list
        volumes.append(volume)

    # Return the list of volumes
    return volumes