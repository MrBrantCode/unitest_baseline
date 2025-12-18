"""
QUESTION:
Write a function to sort a list of student tuples in ascending order by last name, then by first name, and finally by the length of the first name. The input is a list of tuples, where each tuple contains the first name and last name of a student. The function should return a new sorted list of tuples.
"""

def sort_students(students):
    """
    Sorts a list of student tuples in ascending order by last name, then by first name, and finally by the length of the first name.

    Args:
        students (list): A list of tuples, where each tuple contains the first name and last name of a student.

    Returns:
        list: A new sorted list of tuples.
    """
    return sorted(students, key=lambda x: (x[1], x[0], len(x[0])))