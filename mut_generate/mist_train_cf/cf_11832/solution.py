"""
QUESTION:
Create a function called `create_grade_dictionary` that takes two lists, `student_ids` and `grades`, as input. The function should return a dictionary where the keys are the student IDs and the corresponding values are their grades. The student IDs are unique integers, and the grades are floating-point numbers between 0 and 100. If the lengths of the input lists are not equal, the function should assign `None` as the grade for the remaining student IDs. The function should have a time complexity of O(n), where n is the length of the longer input list.
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