"""
QUESTION:
Write a function `grade_transform(num_score)` that takes an integer score between 1 and 100 and returns its corresponding alphabetic grade. The grade scale is as follows:
- 90-100: 'A'
- 80-89: 'B'
- 70-79: 'C'
- 60-69: 'D'
- Below 60: 'F'
"""

def grade_transform(num_score):
    if num_score >= 90:  
        return "A"
    elif num_score >= 80:  
        return "B"
    elif num_score >= 70:  
        return "C"
    elif num_score >= 60:  
        return "D"
    else:  
        return "F"