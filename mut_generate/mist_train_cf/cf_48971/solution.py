"""
QUESTION:
Calculate the weighted GPA from a list of courses with their corresponding scores and credit hours, considering additional grace marks. Implement a function `weighted_gpa(score_weight_list)` that takes a list of tuples, where each tuple contains the course name, score, and credit hours. The function should calculate the weighted GPA using the credit hours as weights. Also, implement a function `grade_from_score(score)` that assigns a grade ("A", "B", "C") based on the given score, with scores 95 and above being "A", 85-94 being "B", and below 85 being "C".
"""

def calculate_weighted_gpa(score_weight_list):
    """Calculate the weighted GPA from a list of courses with their corresponding scores and credit hours."""
    total_credit_hours = sum([x[2] for x in score_weight_list])
    score_weight_sum = sum([score * credit_hours for _, score, credit_hours in score_weight_list])
    return score_weight_sum / total_credit_hours

def assign_grade(score):
    """Assign a grade ("A", "B", "C") based on the given score."""
    if score >= 95:
        return 'A'
    elif score >= 85:
        return 'B'
    else:
        return 'C'