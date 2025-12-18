"""
QUESTION:
Create a function `sort_students` that takes a list of student tuples, where each tuple contains the first name and last name of a student. Sort the list of students alphabetically by their last name. If two students have the same last name, sort them by their first name. If the first names are also the same, sort them by the length of their first name in ascending order.
"""

def sort_students(students):
    """
    Sorts a list of student tuples alphabetically by their last name.
    If two students have the same last name, sorts them by their first name.
    If the first names are also the same, sorts them by the length of their first name in ascending order.
    
    Args:
        students (list): A list of tuples containing the first name and last name of students.
    
    Returns:
        list: A sorted list of student tuples.
    """
    return sorted(students, key=lambda x: (x[1], x[0], len(x[0])))