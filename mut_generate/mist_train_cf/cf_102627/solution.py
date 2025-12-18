"""
QUESTION:
Write a function that calculates the average age of students with a grade higher than 80. The function should take no arguments and return the result sorted in descending order of age.
"""

def calculate_average_age(students):
    """
    Calculate the average age of students with a grade higher than 80.

    Args:
        students (list): A list of dictionaries where each dictionary represents a student with 'age' and 'grade' keys.

    Returns:
        dict: A dictionary with 'average_age' key and the calculated average age as the value. The result is sorted in descending order of age.
    """
    eligible_students = [student for student in students if student['grade'] > 80]
    eligible_students.sort(key=lambda x: x['age'], reverse=True)
    
    if not eligible_students:
        return {'average_age': None}

    average_age = sum(student['age'] for student in eligible_students) / len(eligible_students)
    return {'average_age': average_age}