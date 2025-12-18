"""
QUESTION:
Calculate the weighted GPA from a list of test scores. The list contains tuples with the course name and the corresponding test score, and each course has a weight associated with it, ranging from 1 to 10. The function should multiply each test score by its corresponding weight, sum these products, and then divide by the sum of the weights. A course's test score must be 80 or higher to be included in the calculation. 

The function name should be `calculate_weighted_gpa`. The function takes a list of tuples as input where each tuple contains a course name and a test score.
"""

def calculate_weighted_gpa(test_scores):
    weighted_sum = 0
    weight_sum = 0
    for course, score, weight in test_scores:
        if score >= 80:
            weighted_sum += score * weight
            weight_sum += weight
    if weight_sum == 0:
        return 0
    gpa = weighted_sum / weight_sum
    return gpa