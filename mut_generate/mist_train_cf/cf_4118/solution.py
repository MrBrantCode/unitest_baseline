"""
QUESTION:
Design a function named `calculate_average_grade` that takes a list of dictionaries representing students with 'name', 'age', and 'grade' keys. The function should calculate the average grade for each age group and return a dictionary with age groups as keys and their corresponding average grades as values. The function should also identify the age group with the highest average grade and return this age group. The input list of dictionaries may contain any number of student records, and the grades are floating point numbers.
"""

from collections import defaultdict

def calculate_average_grade(students):
    """
    Calculate the average grade for each age group and identify the age group with the highest average grade.

    Args:
        students (list): A list of dictionaries, where each dictionary represents a student with 'name', 'age', and 'grade' keys.

    Returns:
        dict: A dictionary with age groups as keys and their corresponding average grades as values.
        int: The age group with the highest average grade.
    """
    age_groups = defaultdict(list)
    for student in students:
        age_groups[student['age']].append(student['grade'])
    
    average_grades = {}
    highest_average_grade = 0
    highest_average_grade_age_group = None
    for age, grades in age_groups.items():
        average_grade = sum(grades) / len(grades)
        average_grades[age] = average_grade
        if average_grade > highest_average_grade:
            highest_average_grade = average_grade
            highest_average_grade_age_group = age
    
    return average_grades, highest_average_grade_age_group