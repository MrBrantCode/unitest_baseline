"""
QUESTION:
Create a function called `get_students_above_threshold` that takes a list of tuples, where each tuple contains a student's name and marks, and a threshold value. The function should return a list of names of students who have secured more than the given threshold marks. Additionally, the program should calculate and display the average marks of all the students, total number of students, highest marks obtained by any student, lowest marks obtained by any student, and standard deviation of the marks. The program should also allow user input to add more students to the list. The threshold value is 80.
"""

import math

def get_students_above_threshold(students, threshold):
    above_threshold_students = []
    for student in students:
        if student[1] > threshold:
            above_threshold_students.append(student[0])
    return above_threshold_students