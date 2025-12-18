"""
QUESTION:
Create a function `sort_students` that takes an array of student objects as input. Each student object has properties `name`, `age`, and `grades` (an array of 10 grades ranging from 0 to 100). The function should calculate the average grade for each student by dividing the sum of their grades by 10, and then sort the students in descending order based on their average grade. If two or more students have the same average grade, they should be further sorted in ascending order based on their age. If two or more students have the same average grade and age, they should be further sorted in alphabetical order based on their name. The function should return a list of student names in the sorted order.
"""

def sort_students(students):
    """
    Sorts a list of student objects based on their average grade, age, and name.

    Args:
        students (list): A list of student objects with properties name, age, and grades.

    Returns:
        list: A list of student names in the sorted order.
    """
    # Calculate the average grade for each student and add it as a property
    for student in students:
        student['averageGrade'] = sum(student['grades']) / 10
    
    # Sort the students based on average grade, age, and name
    sorted_students = sorted(students, key=lambda x: (-x['averageGrade'], x['age'], x['name']))
    
    # Return a list of student names in the sorted order
    return [student['name'] for student in sorted_students]