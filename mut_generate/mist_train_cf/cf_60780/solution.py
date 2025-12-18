"""
QUESTION:
Write a function `calculate_sum_octagon` that takes five arguments representing the degree measurements of five angles in an irregular octagon and returns the sum of the degree measurements of the remaining three angles. Assume the total interior angle sum of the octagon is 1080 degrees.
"""

def calculate_sum_octagon(angle1, angle2, angle3, angle4, angle5):
    """
    Calculate the sum of the degree measurements of the remaining three angles in an irregular octagon.

    Args:
        angle1 (int): Degree measurement of the first angle.
        angle2 (int): Degree measurement of the second angle.
        angle3 (int): Degree measurement of the third angle.
        angle4 (int): Degree measurement of the fourth angle.
        angle5 (int): Degree measurement of the fifth angle.

    Returns:
        int: The sum of the degree measurements of the remaining three angles.
    """
    total_angles_octagon = 1080
    sum_given_angles = angle1 + angle2 + angle3 + angle4 + angle5
    return total_angles_octagon - sum_given_angles