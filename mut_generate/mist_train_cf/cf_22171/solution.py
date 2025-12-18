"""
QUESTION:
Create a function named `calculate_max_height` to calculate the maximum height reached by a ball thrown upward. The function should take into account air resistance and wind direction, and consider the effect of different air densities at different altitudes.
"""

def calculate_max_height(velocity, mass, drag_coefficient, cross_sectional_area, air_density, wind_speed=0, wind_direction=0):
    """
    Calculate the maximum height reached by a ball thrown upward.

    Args:
    velocity (float): Initial velocity of the ball (m/s).
    mass (float): Mass of the ball (kg).
    drag_coefficient (float): Drag coefficient of the ball.
    cross_sectional_area (float): Cross-sectional area of the ball (m^2).
    air_density (float): Air density at sea level (kg/m^3).
    wind_speed (float, optional): Wind speed (m/s). Defaults to 0.
    wind_direction (float, optional): Wind direction (radians). Defaults to 0.

    Returns:
    float: Maximum height reached by the ball (m).
    """

    # Calculate the acceleration due to air resistance
    acceleration_due_to_air_resistance = 0.5 * drag_coefficient * air_density * cross_sectional_area * velocity**2 / mass

    # Calculate the acceleration due to wind
    acceleration_due_to_wind = wind_speed * math.cos(wind_direction)

    # Calculate the net acceleration
    net_acceleration = -9.81 - acceleration_due_to_air_resistance + acceleration_due_to_wind

    # Calculate the maximum height
    max_height = (velocity**2) / (2 * abs(net_acceleration))

    return max_height