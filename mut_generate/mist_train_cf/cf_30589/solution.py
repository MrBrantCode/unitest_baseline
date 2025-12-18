"""
QUESTION:
Write a function `process_scores(scores, threshold)` that takes in a list of dictionaries representing students' exam scores and an integer representing the passing threshold for the exams. Each dictionary should contain the keys 'name' (string), 'math' (integer), 'science' (integer), and 'history' (integer). The function should return a JSON response where each key-value pair represents a student's name and whether their average score (rounded to the nearest integer) is greater than or equal to the threshold (True) or less than the threshold (False).
"""

def process_scores(scores, threshold):
    response = {}
    for student in scores:
        average_score = round((student['math'] + student['science'] + student['history']) / 3)
        response[student['name']] = average_score >= threshold
    return response