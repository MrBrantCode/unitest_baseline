"""
QUESTION:
Create a function named `create_grade_dictionary` that takes two lists of integers and floats as input, `student_ids` and `grades`, and returns a dictionary. The function should map each student ID to its corresponding grade and handle cases where the input lists are of unequal lengths. If a student ID has no corresponding grade, map it to `None`. The time complexity of the function should be O(n), where n is the length of the longer input list.
"""

def create_grade_dictionary(student_ids, grades):
    # Create an empty dictionary
    grade_dict = {}
    
    # Get the length of the longer list
    length = max(len(student_ids), len(grades))
    
    # Loop through the indices of the longer list
    for i in range(length):
        # Check if the index is within the range of student_ids
        if i < len(student_ids):
            # Get the student ID and grade at the current index
            student_id = student_ids[i]
            grade = grades[i] if i < len(grades) else None
            
            # Add the student ID and grade to the dictionary
            grade_dict[student_id] = grade
    
    return grade_dict