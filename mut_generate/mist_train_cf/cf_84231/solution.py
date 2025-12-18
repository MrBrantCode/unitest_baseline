"""
QUESTION:
Write a function `calculate_weighted_gpa` that takes a list of tuples as input, where each tuple contains a course's score, credit hours, and weightage in the final score. The function should calculate the weighted GPA, considering the weightages and credit hours. The weightages are percentage values and should be normalized by dividing by 100. The GPA is on a scale of 100.
"""

def calculate_weighted_gpa(courses):
    total_weighted_score = 0
    total_credit_hours = 0
    for course in courses:
        score = course[0]
        credit_hours = course[1]
        weightage = course[2]
        weightage_score = (score * weightage) / 100
        total_weighted_score += weightage_score * credit_hours
        total_credit_hours += credit_hours
    return total_weighted_score / total_credit_hours