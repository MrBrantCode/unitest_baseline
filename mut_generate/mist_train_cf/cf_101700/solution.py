"""
QUESTION:
Write a function called `calculate_third_angle` that takes two angles of a triangle in degrees as input and returns the third angle in degrees. The input will be a JSON object with the two angles represented as "angle1" and "angle2", and the output should also be in JSON format with the calculated third angle represented as "angle3". The sum of the angles in a triangle is 180 degrees.
"""

import json

def calculate_third_angle(input_json):
    """
    Calculate the third angle in a triangle given two angles in degrees.

    Args:
        input_json (str): A JSON object containing "angle1" and "angle2".

    Returns:
        str: A JSON object containing the calculated "angle3".
    """
    input_data = json.loads(input_json)
    angle1 = input_data['angle1']
    angle2 = input_data['angle2']
    angle3 = 180 - angle1 - angle2
    return json.dumps({'angle3': angle3})