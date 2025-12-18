"""
QUESTION:
Write a function `calculate_third_angle` that takes two angles in degrees as input and returns the third angle in a triangle. The input and output should be in JSON format, where the input contains "angle1" and "angle2" keys, and the output contains the calculated value of the third angle as "angle3".
"""

import json

def calculate_third_angle(input_json):
    angle1 = input_json['angle1']
    angle2 = input_json['angle2']
    angle3 = 180 - angle1 - angle2
    return json.dumps({'angle3': angle3})