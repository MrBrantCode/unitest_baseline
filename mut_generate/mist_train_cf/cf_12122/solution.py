"""
QUESTION:
Create a Python class called Student with an initializer method that takes in the name, age, and marks of a student as parameters and sets them as instance variables. The class should have three methods: calculate_average(total_marks, num_subjects) to calculate the average marks of the student, display_information() to print the student's information, and is_eligible_for_scholarship(threshold) to check if the student's average marks are above a certain threshold. The average marks should be calculated by dividing the total marks by the number of subjects taken. The student is eligible for a scholarship if their average marks are greater than or equal to the threshold.
"""

def entrance(total_marks, num_subjects, threshold):
    average_marks = total_marks / num_subjects
    return average_marks >= threshold