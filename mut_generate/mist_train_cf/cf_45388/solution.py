"""
QUESTION:
Create a function `numeric_to_letter_grade(score)` that takes a numerical score between 1 and 100 and returns its corresponding linguistic grade characterization. The grading scale is as follows: 
- 1-59: Fail 
- 60-69: D 
- 70-79: C 
- 80-89: B 
- 90-100: A 
If the score is outside the range of 1 to 100, the function should return "Invalid score. It should be between 1 and 100."
"""

def numeric_to_letter_grade(score):
    if score < 0 or score > 100:
        return "Invalid score. It should be between 1 and 100."
    elif score < 60:
        return "Fail"
    elif score < 70:
        return "D"
    elif score < 80:
        return "C"
    elif score < 90:
        return "B"
    else:
        return "A"