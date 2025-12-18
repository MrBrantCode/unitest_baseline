"""
QUESTION:
Create a function `generate_class_list` that generates a list of unique student names in alphabetical order, with a maximum length of 10.
"""

def generate_class_list(students):
    """
    Generate a list of unique student names in alphabetical order, with a maximum length of 10.
    
    Args:
        students (list): A list of student names.
    
    Returns:
        list: A list of unique student names in alphabetical order, with a maximum length of 10.
    """
    unique_students = set(students)
    sorted_students = sorted(list(unique_students))
    return sorted_students[:10]