"""
QUESTION:
Write a function named `fill_tank_time` that calculates the time required for two hydraulic conduits to fill a storage tank when operating concomitantly. The function should take two parameters: `time1` and `time2`, representing the time in hours it takes for the first and second conduits to fill the tank individually.
"""

def fill_tank_time(time1, time2):
    # Calculate the combined rate at which the two conduits fill the tank
    combined_rate = 1 / time1 + 1 / time2
    
    # Calculate the time it takes to fill the tank at the combined rate
    return 1 / combined_rate