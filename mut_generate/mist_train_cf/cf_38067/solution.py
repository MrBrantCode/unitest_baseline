"""
QUESTION:
Given a list of image paths in the format "path/to/image_xxx.jpg" where "xxx" is a three-digit number indicating the brightness level, write a function `average_brightness(image_paths)` that takes the list of image paths as input and returns the average brightness of the images.
"""

def entrance(image_paths):
    total_brightness = 0
    for path in image_paths:
        brightness = float(path[-7:-4])  # Extract the brightness level from the file name
        total_brightness += brightness
    return total_brightness / len(image_paths)  # Calculate the average brightness