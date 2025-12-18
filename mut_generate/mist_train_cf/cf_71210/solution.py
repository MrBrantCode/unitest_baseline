"""
QUESTION:
Create a function called `create_student_dict` that takes two parameters: `student_ids` and `grades`, both of which are lists of values. The function should return a dictionary with the values in `student_ids` as keys and the corresponding values in `grades` as values. If the lengths of `student_ids` and `grades` are not equal, the function should return an error message. Additionally, all values in `student_ids` must be integers and all values in `grades` must be numeric (either integers or floats); if not, the function should return an error message.
"""

def create_student_dict(student_ids, grades):
    """
    This function creates a dictionary with student IDs as keys and grades as values.
    
    Parameters:
    student_ids (list): A list of integers representing student IDs.
    grades (list): A list of numeric values representing grades.
    
    Returns:
    dict or str: A dictionary with student IDs as keys and grades as values, or an error message.
    """
    
    # Check if the lengths of the input lists are equal
    if len(student_ids) != len(grades):
        return "Error: The lengths of the lists are not equal."
    
    # Initialize an empty dictionary to store student IDs and grades
    student_dict = {}
    
    # Iterate over the input lists
    for i in range(len(student_ids)):
        # Check if each student ID is an integer and each grade is a numeric value
        if not isinstance(student_ids[i], int) or not isinstance(grades[i], (int, float)):
            return "Error: All student IDs must be integers and all grades must be numeric."
        
        # Add the student ID and grade to the dictionary
        student_dict[student_ids[i]] = grades[i]
    
    # Return the dictionary
    return student_dict