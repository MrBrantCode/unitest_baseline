"""
QUESTION:
Write a function that calculates the percentage of correct answers for each student from a normalized answer table and returns the students with a score above a certain threshold. The function should take a student ID, a set of correct answers, and the answers provided by each student as input, and return a list of student IDs and their corresponding scores. The function should be efficient and scalable.
"""

def entrance(correct_answers, answers, threshold):
    """
    This function calculates the percentage of correct answers for each student 
    from a normalized answer table and returns the students with a score above 
    a certain threshold.

    Parameters:
    correct_answers (list): A list of correct answers.
    answers (dict): A dictionary where the keys are student IDs and the values 
                    are lists of answers provided by each student.
    threshold (float): The minimum score required for a student to be included 
                       in the result.

    Returns:
    list: A list of tuples where the first element is the student ID and the 
          second element is the student's score.
    """
    
    # Initialize an empty list to store the student IDs and their scores
    scored_students = []
    
    # Iterate over each student ID and their answers
    for student_id, student_answers in answers.items():
        # Calculate the number of correct answers
        correct_count = sum(1 for correct, answer in zip(correct_answers, student_answers) if correct == answer)
        
        # Calculate the percentage of correct answers
        score = (correct_count / len(correct_answers)) * 100
        
        # Check if the student's score is above the threshold
        if score > threshold:
            # Add the student ID and score to the list
            scored_students.append((student_id, score))
    
    # Return the list of student IDs and their scores
    return scored_students