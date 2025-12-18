"""
QUESTION:
Create a function called `add_student_prefix` that takes a list of dictionaries as input, where each dictionary represents a student with 'name' and 'grade' keys. The function should return a new list of dictionaries where the string "student_" is added to the beginning of each student's name if their grade is higher than 80. The returned list should be sorted in descending order based on the student's grade.
"""

def add_student_prefix(students):
    """
    Adds 'student_' prefix to student names with grades higher than 80 and returns the list sorted by grade in descending order.

    Args:
        students (list): A list of dictionaries, each containing 'name' and 'grade' keys.

    Returns:
        list: A new list of dictionaries with 'student_' prefix added to names with grades higher than 80, sorted by grade in descending order.
    """
    return sorted([{"name": "student_" + student['name'], "grade": student['grade']} if student['grade'] > 80 else student for student in students], key=lambda x: x['grade'], reverse=True)