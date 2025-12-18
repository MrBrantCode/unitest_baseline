"""
QUESTION:
Design a function `find_improved_students` to identify students who secured more than 80% marks and improved their scores by more than 10% from their best previous score. The function should accept a list of student dictionaries as input, where each dictionary contains the student's name, a list of previous scores, and their current score. The function should return a list of dictionaries containing the names, current scores, and percentage improvements of the improved students.
"""

def find_improved_students(students):
    """
    This function identifies students who secured more than 80% marks and improved their scores by more than 10% from their best previous score.

    Args:
    students (list): A list of dictionaries, where each dictionary contains the student's name, a list of previous scores, and their current score.

    Returns:
    list: A list of dictionaries containing the names, current scores, and percentage improvements of the improved students.
    """

    improved_students = []
    
    # Iterate over each student in the list
    for student in students:
        # Check if current score is more than 80
        if student['current_score'] > 80:
            # Find maximum score in previous scores
            best_prev_score = max(student['prev_scores'])
            # Calculate improvement
            improvement = (student['current_score'] - best_prev_score) / best_prev_score * 100
            # Check if improvement is more than 10%
            if improvement > 10:
                # Append the improved student's info to the list
                improved_students.append({"Name": student['name'], "Current Score": student['current_score'], "Improvement": improvement})
    
    # Return the list of improved students
    return improved_students