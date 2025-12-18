"""
QUESTION:
Write a function named `calculate_third_angle` that takes a dictionary containing two angles ("angle1" and "angle2") of a triangle as input and returns a dictionary with the calculated third angle ("angle3") in degrees. The sum of the three angles in the triangle should be 180 degrees.
"""

def calculate_third_angle(input_json):
    """
    Calculate the third angle of a triangle given two angles.
    
    Args:
        input_json (dict): A dictionary containing "angle1" and "angle2" in degrees.
    
    Returns:
        dict: A dictionary containing the calculated "angle3" in degrees.
    """
    angle1 = input_json['angle1']
    angle2 = input_json['angle2']
    angle3 = 180 - angle1 - angle2
    return {'angle3': angle3}