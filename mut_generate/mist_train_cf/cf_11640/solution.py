"""
QUESTION:
Write a function `calculate_average` that takes a list of student grades as input. The function should calculate the average of grades that are above 70, and return this average along with the highest grade among the valid grades. If there are no grades above 70, the function should return a message indicating that there are no valid grades.
"""

def calculate_average(grades):
    valid_grades = [grade for grade in grades if grade > 70]
    
    if len(valid_grades) == 0:
        return "There are no valid grades."
    
    return sum(valid_grades) / len(valid_grades), max(valid_grades)