"""
QUESTION:
Create a function called "calculate_average_grade" that takes a dictionary as a parameter where each key is a student's name and each value is a list of integers representing the student's grades in different subjects. The function should return a new dictionary where the keys are the student names and the values are their average grades rounded to two decimal places.

The function should handle the following restrictions:

- If the input dictionary is empty, return "Error: Dictionary is empty."
- If a student's grade list is empty, include the student in the output dictionary with the value "Error: No grades available."
- If a student's grade list contains negative values, ignore them and calculate the average grade based on the remaining non-negative values. If all grades are negative, include the student in the output dictionary with the value "Error: No valid grades available."
"""

def calculate_average_grade(grades_dict):
    if not grades_dict:
        return "Error: Dictionary is empty."
    
    average_grades = {}
    for student, grades in grades_dict.items():
        if not grades:
            average_grades[student] = "Error: No grades available."
        else:
            valid_grades = [grade for grade in grades if grade >= 0]
            if not valid_grades:
                average_grades[student] = "Error: No valid grades available."
            else:
                average = round(sum(valid_grades) / len(valid_grades), 2)
                average_grades[student] = average
    return average_grades