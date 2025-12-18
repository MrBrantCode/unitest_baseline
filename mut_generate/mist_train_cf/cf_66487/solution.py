"""
QUESTION:
Write a function `calculate_gpa` that takes in a list of test scores `test_scores` and a grading system `grading_system`. The `test_scores` list consists of tuples containing course name, score, credit hours, and grade. The `grading_system` is a dictionary mapping grades to their respective points. Calculate and return the weighted GPA, considering the credit hours and grading system. The weighted GPA is calculated by summing up the product of grade points and credit hours for each course, then dividing by the total credit hours.
"""

def calculate_gpa(test_scores, grading_system):
    total_credits = 0
    weighted_scores = 0
    for course in test_scores:
        score = course[1]
        credits = course[2]
        grade = course[3]
        
        total_credits += credits
        weighted_scores += grading_system[grade] * credits
    
    gpa = weighted_scores / total_credits
    return gpa