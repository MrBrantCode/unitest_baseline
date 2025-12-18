"""
QUESTION:
Create a function `sort_students` that takes an array of student objects as input and returns the array sorted in descending order based on the age of the students. If two students have the same age, they should be sorted alphabetically based on their names. Each student object should contain the properties 'name', 'age', 'grade', and 'subjects'.
"""

def sort_students(students):
    """
    Sorts an array of student objects in descending order based on age.
    If two students have the same age, they are sorted alphabetically by name.

    Args:
        students (list): A list of student objects.
            Each student object should contain the properties 'name', 'age', 'grade', and 'subjects'.

    Returns:
        list: The sorted list of student objects.
    """
    return sorted(students, key=lambda x: (-x['age'], x['name']))