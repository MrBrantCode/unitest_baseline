"""
QUESTION:
Write a function that takes a list of tuples, where each tuple contains a student's name and marks. The function should return the names of students who have secured more than 80% marks. The function should also calculate and display the average marks of all the students, total number of students, highest marks obtained by any student, lowest marks obtained by any student, and standard deviation of the marks. The function should allow user input to add more students to the list.
"""

import math

def entrance(students):
    """
    This function takes a list of tuples, where each tuple contains a student's name and marks.
    It returns the names of students who have secured more than 80% marks and calculates 
    the average marks of all the students, total number of students, highest marks obtained 
    by any student, lowest marks obtained by any student, and standard deviation of the marks.

    Args:
        students (list): A list of tuples containing student's name and marks.

    Returns:
        tuple: A tuple containing the names of students with more than 80% marks, average marks, 
        total number of students, highest marks, lowest marks, and standard deviation.
    """

    # Calculate average marks
    total_marks = sum([marks for _, marks in students])
    average_marks = total_marks / len(students)

    # Calculate total number of students
    total_students = len(students)

    # Calculate highest marks
    highest_marks = max([marks for _, marks in students])

    # Calculate lowest marks
    lowest_marks = min([marks for _, marks in students])

    # Calculate standard deviation
    mean = average_marks
    variance = sum([((marks - mean) ** 2) for _, marks in students]) / len(students)
    standard_deviation = math.sqrt(variance)

    # Get names of students with more than 80% marks
    students_with_high_marks = [name for name, marks in students if marks > 80]

    return (students_with_high_marks, average_marks, total_students, highest_marks, lowest_marks, standard_deviation)