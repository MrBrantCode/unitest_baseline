"""
QUESTION:
Create a function named `academic_grade` that calculates the academic grade of a student based on the cumulative score across multiple disciplines with varying weightage for each discipline. The function should accept two lists as arguments: `scores` and `weightage`, where `scores` contains the scores in each discipline and `weightage` contains the relative weightage of each discipline. The function should handle any number of elements in the input lists, and the lists must be of the same size. The grades are determined by the following weighted average score ranges: 90 and above is 'A', 80-89 is 'B', 70-79 is 'C', 60-69 is 'D', and below 60 is 'F'.
"""

def entrance(scores, weightage):
    # First check if scores and weightage lists sizes match
    if len(scores) != len(weightage):
        return "Scores and weightage input lists must be of the same size!"
    
    # Initialize weighted sum
    weighted_sum = 0

    # Calculate weighted sum
    for i in range(len(scores)):
        weighted_sum += scores[i] * weightage[i]
    
    # Determine grade based on weighted average score
    if weighted_sum >= 90:
        grade = 'A'
    elif weighted_sum >= 80:
        grade = 'B'
    elif weighted_sum >= 70:
        grade = 'C'
    elif weighted_sum >= 60:
        grade = 'D'
    else:
        grade = 'F'

    return grade