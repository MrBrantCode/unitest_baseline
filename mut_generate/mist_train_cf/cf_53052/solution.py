"""
QUESTION:
Implement a function `line` that takes in a destination value, a time interval, and an optional grain value. The function should return a list of values representing the linear ramp from 0 to the destination value over the given time interval, with the "resolution" of the ramp determined by the grain value. The grain value specifies the time interval between each output from the line, effectively controlling the smoothness of the ramp.
"""

def line(destination, time_interval, grain=0.01):
    """
    Returns a list of values representing the linear ramp from 0 to the destination value 
    over the given time interval, with the "resolution" of the ramp determined by the grain value.

    Args:
        destination (float): The destination value of the linear ramp.
        time_interval (float): The time interval over which the linear ramp is executed.
        grain (float, optional): The time interval between each output from the line. Defaults to 0.01.

    Returns:
        list: A list of values representing the linear ramp.
    """
    steps = int(time_interval / grain)
    values = [i * destination / steps for i in range(steps + 1)]
    return values