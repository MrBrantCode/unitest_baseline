"""
QUESTION:
Implement a function `calculate_grade_and_gpa` that takes a numerical grade as input and returns the corresponding letter grade and grade point equivalent (GPA) on a scale of 4.0. The GPA should be calculated with consideration of fractions. 

The letter grade and GPA mapping should follow these ranges: 
- A: 90-100, GPA: 4.0
- B: 80-89, GPA: 3.0 - 4.0
- C: 70-79, GPA: 2.0 - 3.0
- D: 60-69, GPA: 1.0 - 2.0
- F: <60, GPA: 0.0

The GPA should be rounded to two decimal places.
"""

def calculate_grade_and_gpa(numerical_grade):
    if numerical_grade >= 90:
        letter_grade = "A"
        gpa = 4.0
    elif 80 <= numerical_grade < 90:
        letter_grade = "B"
        gpa = 3.0 + (numerical_grade - 80) / 10
    elif 70 <= numerical_grade < 80:
        letter_grade = "C"
        gpa = 2.0 + (numerical_grade - 70) / 10
    elif 60 <= numerical_grade < 70:
        letter_grade = "D"
        gpa = 1.0 + (numerical_grade - 60) / 10
    else:
        letter_grade = "F"
        gpa = 0.0

    return letter_grade, round(gpa, 2)