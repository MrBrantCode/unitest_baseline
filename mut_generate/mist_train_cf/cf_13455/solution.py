"""
QUESTION:
Create a function named `meets_criteria` that takes a list of student records as input. Each student record is a dictionary containing 'name', 'score', and 'grade_level'. The 'score' should be an integer and 'grade_level' should be a positive integer between 1 and 12. The function should return a list of student names who have a score above 80 and a grade level of 10 or above, ignoring any invalid student records.
"""

def meets_criteria(students):
    """
    This function filters a list of student records and returns a list of student names who have a score above 80 and a grade level of 10 or above.
    
    Args:
    students (list): A list of student records. Each record is a dictionary containing 'name', 'score', and 'grade_level'.
    
    Returns:
    list: A list of student names who meet the criteria.
    """
    
    # Function to check if a student record is valid
    def is_valid_student(record):
        if 'name' not in record or 'score' not in record or 'grade_level' not in record:
            return False
        if not isinstance(record['score'], int) or not isinstance(record['grade_level'], int):
            return False
        if record['grade_level'] < 1 or record['grade_level'] > 12:
            return False
        return True

    # Filter the student records and return the names of students who meet the criteria
    return [record['name'] for record in students if is_valid_student(record) and record['score'] > 80 and record['grade_level'] >= 10]