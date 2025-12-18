"""
QUESTION:
Implement a function `highest_average_grade` that takes a non-empty list of `Student` objects, where each `Student` has a `name` and a list of `grades`. Calculate the average grade for each student and return the name of the student with the highest average grade. If multiple students have the same highest average grade, return the name of the first student encountered in the list.
"""

from typing import List

class Student:
    def __init__(self, name: str, grades: List[int]):
        self.name = name
        self.grades = grades

def highest_average_grade(students: List[Student]) -> str:
    max_average = 0
    top_student = ""
    
    for student in students:
        average_grade = sum(student.grades) / len(student.grades)
        if average_grade > max_average:
            max_average = average_grade
            top_student = student.name
    
    return top_student