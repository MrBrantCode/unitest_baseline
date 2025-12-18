"""
QUESTION:
Create a function named `ideal_sensitivity` that takes two parameters: `dpi` (the dots per inch of a mouse) and `resolution` (the resolution of a monitor, represented as a tuple of two integers). The function should calculate and return the ideal mouse sensitivity for playing Rainbow Six Siege, considering the total number of pixels on the monitor, the number of pixels the mouse moves for a 360-degree turn, and assuming a default 360-degree distance of 39.37 inches (100 cm) and a 16:9 aspect ratio.
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