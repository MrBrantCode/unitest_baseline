"""
QUESTION:
Write a Python function named `recommend_method` that takes two parameters: `subject` (a string representing the subject) and `rating` (an integer between 0 and 10 representing the student's rating). Based on the subject and rating, return a string recommending a teaching method. If the subject is 'Mathematics' and the rating is 8 or above, recommend 'Clear explanations, problem-solving exercises, encouraging questions and discussions'. If the subject is 'Mathematics' but the rating is below 8, recommend 'More practice exercises, one-on-one tutoring, reviewing fundamentals'. For any other subject, return 'No recommendation available'.
"""

def recommend_method(subject, rating):
    if subject == 'Mathematics':
        if rating >= 8:
            return 'Clear explanations, problem-solving exercises, encouraging questions and discussions'
        else:
            return 'More practice exercises, one-on-one tutoring, reviewing fundamentals'
    else:
        return 'No recommendation available'