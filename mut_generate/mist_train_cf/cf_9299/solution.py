"""
QUESTION:
Write a function named 'filter_students' that filters records from a table named 'StudentTable' based on specific criteria. The function should include only students who have a GPA greater than 3.5 and are enrolled in the Computer Science program.
"""

def filter_students(students):
    """
    Filters students with GPA greater than 3.5 and enrolled in the Computer Science program.

    Args:
        students (list): A list of dictionaries containing student information.

    Returns:
        list: A list of dictionaries containing filtered student information.
    """
    return [student for student in students if student['GPA'] > 3.5 and student['Program'] == 'Computer Science']