"""
QUESTION:
Design a function `update_student_names` that efficiently stores a list of students' names, allowing each student to have multiple names and eliminating duplicates. The function should be able to handle name updates when a student decides to change their name.
"""

def update_student_names(student_names, student_id, old_name, new_name):
    """
    Updates a student's name in the student_names set.

    Args:
    student_names (dict): A dictionary where keys are student IDs and values are sets of names.
    student_id (int): The ID of the student whose name needs to be updated.
    old_name (str): The old name of the student that needs to be updated.
    new_name (str): The new name of the student.

    Returns:
    dict: The updated student_names dictionary.
    """
    if student_id not in student_names:
        student_names[student_id] = set()
    
    if old_name in student_names[student_id]:
        student_names[student_id].remove(old_name)
    student_names[student_id].add(new_name)
    return student_names