"""
QUESTION:
Implement the `calculate_average_grades` function that takes a dataset as input, where each element is a tuple containing a student's name (string) and a list of their grades in different subjects (integers). The function should calculate the average grade for each student by summing their grades and dividing by the total number of subjects, round the average to the nearest integer, and return a dictionary where the keys are the student names and the values are their average grades.
"""

def calculate_average_grades(dataset):
    average_grades = {}
    for student, grades in dataset:
        average_grade = round(sum(grades) / len(grades))
        average_grades[student] = average_grade
    return average_grades