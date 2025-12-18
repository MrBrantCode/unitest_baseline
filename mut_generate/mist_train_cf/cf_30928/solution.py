"""
QUESTION:
Write a function `calculate_average_grades` that takes a list of tuples as input, where each tuple contains a student's name as a string and a list of their grades as integers. The function should return a dictionary where the keys are the student names and the values are the average grades for each student. The average grade is calculated by summing up all grades for a student and dividing by the total number of grades. If a student has multiple tuples of grades, they should be combined to calculate the average grade.
"""

from typing import List, Tuple, Dict

def calculate_average_grades(grades: List[Tuple[str, List[int]]]) -> Dict[str, float]:
    average_grades = {}
    count_grades = {}
    
    for student, grade_list in grades:
        if student in average_grades:
            average_grades[student] += sum(grade_list)
            count_grades[student] += len(grade_list)
        else:
            average_grades[student] = sum(grade_list)
            count_grades[student] = len(grade_list)
    
    for student in average_grades:
        average_grades[student] /= count_grades[student]
    
    return average_grades