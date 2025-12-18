"""
QUESTION:
Write a function to find the student with the highest marks in a given subject. The function should return the student's ID and name. The query should join the 'students' table and 'marks' table on 'student_id' where the subject matches the given subject, order the results by marks in descending order, and return only the top result.
"""

def top_student(subject):
    """
    This function returns the student's ID and name with the highest marks in a given subject.
    
    Args:
        subject (str): The subject for which we want to find the top student.

    Returns:
        tuple: A tuple containing the ID and name of the top student in the given subject.
    """
    # Assuming we have a database connection and 'students' and 'marks' tables
    # For simplicity, I'll use lists of dictionaries to mimic the tables
    students = [{'id': 1, 'name': 'John'}, {'id': 2, 'name': 'Alice'}, {'id': 3, 'name': 'Bob'}]
    marks = [{'student_id': 1, 'subject': 'Subject1', 'mark': 90}, 
             {'student_id': 2, 'subject': 'Subject1', 'mark': 95}, 
             {'student_id': 3, 'subject': 'Subject1', 'mark': 85}]

    # Filter the marks for the given subject and sort them in descending order
    top_mark = max((mark for mark in marks if mark['subject'] == subject), key=lambda x: x['mark'], default=None)

    # Find the student with the top mark
    top_student = next((student for student in students if student['id'] == top_mark['student_id']), None) if top_mark else None

    return (top_student['id'], top_student['name']) if top_student else None