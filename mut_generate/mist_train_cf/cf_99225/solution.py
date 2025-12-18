"""
QUESTION:
Create a function named `ideal_sensitivity` that takes two parameters: `dpi` (dots per inch) of a mouse and `resolution` (width and height) of a monitor. The function should calculate the ideal mouse sensitivity for playing Rainbow Six Siege by considering the total number of pixels on the monitor and the number of pixels the mouse moves for a 360 degree turn, assuming a 39.37 inch (100 cm) swipe distance. The function should return the sensitivity value in cm/360.
"""

def ideal_sensitivity(dpi, resolution):
    # Calculate the total number of pixels on the monitor
    total_pixels = resolution[0] * resolution[1]
    
    # Calculate the number of pixels the mouse moves for a 360 degree turn
    # The default 360 distance is 39.37 inches (100 cm)
    # Convert dpi to dots per cm
    dots_per_cm = dpi / 2.54
    distance = 100 * dots_per_cm
    pixels_per_360 = distance * resolution[0] / 39.37
    
    # Calculate the sensitivity needed for a 360 degree turn to be a full swipe across the monitor
    sensitivity = pixels_per_360 / total_pixels
    
    # Return the sensitivity in cm/360
    return sensitivity