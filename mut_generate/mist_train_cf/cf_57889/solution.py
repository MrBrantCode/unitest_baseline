"""
QUESTION:
Write a function called `average_score` that takes a list of tuples as input, where each tuple contains a student's name followed by their scores in five subjects. Each score is a string that needs to be converted to a number before calculation. The function should return a dictionary where the key is the student's name and the value is their average score. Handle any potential exceptions that might occur during the conversion process.
"""

def average_score(student_scores):
    avg_scores = {}
    for student in student_scores:
        total = 0
        valid_scores_count = 0
        for score in student[1:]:
            try:
                total += int(score)
                valid_scores_count += 1
            except ValueError:
                continue
        try:
            avg_scores[student[0]] = total / valid_scores_count
        except ZeroDivisionError:
            avg_scores[student[0]] = 0
    return avg_scores