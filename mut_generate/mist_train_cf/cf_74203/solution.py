"""
QUESTION:
Write a function `total_rope_needed` that takes the number of feet, inches, and students as input, and returns the total length of rope needed in feet. The function should convert the rope length from feet and inches to inches, calculate the total length needed, and then convert it back to feet.
"""

def total_rope_needed(feet, inches, students):
    """
    Calculate the total length of rope needed in feet.

    Parameters:
    feet (int): The number of feet of rope each student needs.
    inches (int): The number of inches of rope each student needs.
    students (int): The number of students.

    Returns:
    float: The total length of rope needed in feet.
    """
    # Convert the length of the rope to inches
    rope_length_total_inches = feet * 12 + inches
    
    # Calculate the total length of rope needed
    total_rope_needed = rope_length_total_inches * students
    
    # Convert the total length of rope back to feet
    return total_rope_needed / 12