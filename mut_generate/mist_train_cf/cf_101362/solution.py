"""
QUESTION:
Write a function named `recommend_method` that takes a subject and a student rating (0-10) as input and returns a suitable teaching method based on the subject and rating. For the subject 'Mathematics', if the rating is 8 or above, the function should return 'Clear explanations, problem-solving exercises, encouraging questions and discussions', otherwise it should return 'More practice exercises, one-on-one tutoring, reviewing fundamentals'. For other subjects, the function should return 'No recommendation available'.
"""

def recommend_method(subject, rating):
    if subject == 'Mathematics':
        if rating >= 8:
            return 'Clear explanations, problem-solving exercises, encouraging questions and discussions'
        else:
            return 'More practice exercises, one-on-one tutoring, reviewing fundamentals'
    else:
        return 'No recommendation available'