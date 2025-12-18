"""
QUESTION:
Create a function `visualizeLightLevels` that takes a list of tuples, where each tuple contains a time in 24-hour format (HH:MM) and a light level reading (integer value), and returns a string representing a visual display of the light levels. The visual display should consist of a series of horizontal bars, with the length of each bar corresponding to the light level value and the time of each reading displayed above the corresponding bar. Assume the input list is sorted in ascending order based on the time of the readings. Each unit of light level should be represented by '#'.
"""

def visualizeLightLevels(readings):
    visual_display = ""
    for time, level in readings:
        visual_display += f"{time} |{'#' * level}\n"
    return visual_display