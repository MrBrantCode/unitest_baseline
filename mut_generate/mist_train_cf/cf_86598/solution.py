"""
QUESTION:
Create a function called "sort_students" that sorts a list of dictionaries representing students based on their 'age' in ascending order and then by 'grade' in descending order if the 'age' is the same.
"""

def sort_students(students):
    """
    Sorts a list of dictionaries representing students based on their 'age' in ascending order 
    and then by 'grade' in descending order if the 'age' is the same.

    Args:
        students (list): A list of dictionaries representing students.

    Returns:
        list: A new list with the sorted elements.
    """
    return sorted(students, key=lambda x: (x['age'], -x['grade']))