"""
QUESTION:
Write a function named `calculate_average` that takes a list of grades as input. The function should calculate the average of grades that are above 70, ignoring any grades below or equal to 70. If there are no grades above 70, the function should output "There are no valid grades." Otherwise, it should output the average and the highest grade among the valid grades.
"""

def calculate_average(grades):
    valid_grades = [grade for grade in grades if grade > 70]
    if not valid_grades:
        return "There are no valid grades."
    else:
        total = sum(valid_grades)
        average = total / len(valid_grades)
        highest_grade = max(valid_grades)
        return f"Average: {average}\nHighest grade: {highest_grade}"