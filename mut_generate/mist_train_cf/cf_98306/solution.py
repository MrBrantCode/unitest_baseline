"""
QUESTION:
Write a function `calculate_third_angle` that calculates the third angle in a triangle when given the values of two angles in degrees. The function should take a JSON object with two keys, "angle1" and "angle2", and return a JSON object with the calculated value of the third angle as "angle3".
"""

import json

def calculate_third_angle(input_json):
    """
    Calculate the third angle in a triangle given the values of two angles in degrees.

    Args:
        input_json (dict): A dictionary containing two keys, "angle1" and "angle2".

    Returns:
        dict: A dictionary with the calculated value of the third angle as "angle3".
    """
    angle1 = input_json['angle1']
    angle2 = input_json['angle2']
    angle3 = 180 - angle1 - angle2
    return {'angle3': angle3}