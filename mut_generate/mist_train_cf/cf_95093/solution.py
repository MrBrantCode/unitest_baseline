"""
QUESTION:
Write a function `sort_students(scores)` that takes a dictionary `scores` containing student names as keys and their corresponding scores as values. The function should return a new dictionary with the students sorted in descending order based on their scores. If multiple students have the same score, they should be sorted alphabetically by their names in ascending order.
"""

def sort_students(scores):
    sorted_students = {}
    
    # Sort the students based on their scores in descending order
    sorted_scores = sorted(scores.items(), key=lambda x: (-x[1], x[0]))
    
    # Create a new dictionary with the sorted students
    for student, score in sorted_scores:
        sorted_students[student] = score
    
    return sorted_students