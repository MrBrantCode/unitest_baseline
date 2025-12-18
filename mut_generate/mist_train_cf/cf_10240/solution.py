"""
QUESTION:
Create a function named `storeStudentNames` that stores a list of students' names, considering that each student can have multiple names and there might be duplicate names in the list. The function should be able to handle the storage of multiple names per student efficiently.
"""

def storeStudentNames(student_names):
    """
    Stores a list of students' names, considering that each student can have multiple names 
    and there might be duplicate names in the list.

    Args:
        student_names (list): A list of lists, where each sublist contains a student's names.

    Returns:
        list: A list of lists, where each sublist contains a student's names.
    """
    return [name for student in student_names for name in student]