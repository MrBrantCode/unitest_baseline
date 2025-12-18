"""
QUESTION:
Create a function "calculateGrade" that takes two parameters: total_questions and correct_answers, both of which are required to be numeric. Calculate and return a grade based on the percentage of correct answers, using the following scale:
- A: 90-100%
- B: 80-89%
- C: 70-79%
- D: 60-69%
- F: <60%

Implement exception handling to handle cases where one or both parameters are missing or not numeric.
"""

def calculateGrade(total_questions, correct_answers):
    if total_questions and correct_answers:
        try:
            total_questions = int(total_questions)
            correct_answers = int(correct_answers)
        except ValueError:
            return "Both inputs must be numeric."

        percentage = (correct_answers / total_questions) * 100

        if percentage >= 90:
            return "A"
        elif percentage >= 80:
            return "B"
        elif percentage >= 70:
            return "C"
        elif percentage >= 60:
            return "D"
        else:
            return "F"
    else:
        return "Both inputs are required."