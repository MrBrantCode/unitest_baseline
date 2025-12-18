"""
QUESTION:
Create a function that sorts a list of student objects in descending order based on their average grade. Each student object contains a name and a list of 5 grades ranging from 0 to 100. The average grade is calculated as the sum of all grades divided by 5. The function should return a list of student names in the sorted order. The input list should contain 1000 student objects.
"""

def sort_students_by_average_grade(students):
    """
    Sorts a list of student objects in descending order based on their average grade.

    Args:
        students (list): A list of student objects.
            Each student object contains a name and a list of 5 grades.

    Returns:
        list: A list of student names in the sorted order.
    """
    return sorted([student['name'] for student in sorted(students, key=lambda x: sum(x['grades']) / len(x['grades']), reverse=True)])