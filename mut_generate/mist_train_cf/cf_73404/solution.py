"""
QUESTION:
Write a function `evaluate_grade` that takes a string `grade` as input and returns a corresponding message based on the grade. The function should handle grades "A+", "A", "B", "C", "D", and "F". If the input grade is not one of the above, the function should return a default message.
"""

def evaluate_grade(grade):
    if grade == "A+":
        return "Excellent! Your performance is outstanding."
    elif grade == "A":
        return "Great job! Your performance is above average."
    elif grade == "B":
        return "Good job! Your performance is average."
    elif grade == "C":
        return "You passed, but there is room for improvement."
    elif grade == "D":
        return "Barely passed. Need to work hard."
    else: #incase the grade is "F" 
        return "Failed. Need more study."