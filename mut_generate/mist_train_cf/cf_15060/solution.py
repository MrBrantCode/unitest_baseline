"""
QUESTION:
Create a function `calculate_average_marks` that takes a dictionary `student_mark_dict` as input, where the keys are student names and the values are dictionaries with subject names as keys and lists of marks as values. The function should calculate the average marks for each subject separately, as well as the overall average mark for each student, and return a dictionary with the average marks for each student.
"""

def calculate_average_marks(student_mark_dict):
    average_marks_dict = {}
    
    for student, subject_marks_dict in student_mark_dict.items():
        average_marks = {}
        
        for subject, marks in subject_marks_dict.items():
            average_marks[subject] = sum(marks) / len(marks)
        
        overall_average = sum(average_marks.values()) / len(average_marks)
        
        average_marks['Overall'] = overall_average
        average_marks_dict[student] = average_marks
    
    return average_marks_dict