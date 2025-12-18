"""
QUESTION:
Write a function `calculate_student_ratio(male_ratio, female_ratio, total_students)` that calculates the number of boys and girls in a class given the total number of students and the ratio of boys to girls. The function should return the number of boys and girls as whole numbers, rounded to the nearest whole student. The input parameters are the ratio of boys to girls and the total number of students in the class.
"""

def calculate_student_ratio(male_ratio, female_ratio, total_students):
    boys = round((male_ratio / (male_ratio + female_ratio)) * total_students)
    girls = total_students - boys
    return boys, girls