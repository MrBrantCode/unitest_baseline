"""
QUESTION:
Create a function named 'calculate_student_average' that takes a dictionary with a student's name and their marks as input. The dictionary should contain the student's name as a string and their marks as a dictionary with subject names as keys and marks as values. The function should calculate the average marks, considering missing subject marks as 0. Return the student's name, marks, and average marks.
"""

def calculate_student_average(student):
    """
    Calculate the average marks of a student.
    
    Args:
    student (dict): A dictionary containing the student's name and their marks.
    
    Returns:
    dict: A dictionary containing the student's name, marks, and average marks.
    """
    
    # Initialize total marks and number of subjects
    total_marks = 0
    number_of_subjects = 0
    
    # Define all subjects
    all_subjects = ["maths", "physics", "chemistry", "biology"]
    
    # Iterate over all subjects to handle missing marks
    for subject in all_subjects:
        if subject in student["marks"]:
            total_marks += student["marks"][subject]
        else:
            student["marks"][subject] = 0
            total_marks += student["marks"][subject]
        number_of_subjects += 1
    
    # Calculate average marks
    average_marks = total_marks / number_of_subjects
    
    # Return the student's name, marks, and average marks
    return {
        "name": student["name"],
        "marks": student["marks"],
        "average_marks": average_marks
    }