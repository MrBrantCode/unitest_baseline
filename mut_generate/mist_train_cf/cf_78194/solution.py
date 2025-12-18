"""
QUESTION:
Write a function `calculate_hobby_age` that takes a JSON array of student objects as input. Each student object contains a 'studentAge' and a 'hobbies' array, where each hobby object contains a 'hobbyAge'. The function should return the total age of all hobbies pursued by students younger than 25 years old and the average hobby age rounded to the nearest integer.
"""

def calculate_hobby_age(students):
    """
    Calculate the total age of all hobbies pursued by students younger than 25 years old 
    and the average hobby age rounded to the nearest integer.

    Args:
        students (list): A list of student objects. Each student object contains a 'studentAge' 
                         and a 'hobbies' array, where each hobby object contains a 'hobbyAge'.

    Returns:
        tuple: A tuple containing the total age of all hobbies and the average hobby age.
    """
    # Initialize total age and count of hobbies
    total_age = 0
    total_hobbies = 0

    # Traverse through each student
    for student in students:
        # Check if student is younger than 25
        if student['studentAge'] < 25:
            # Traverse through each hobby of the student
            for hobby in student['hobbies']:
                # Add the hobby age to the total
                total_age += hobby['hobbyAge']
                # Count the hobby
                total_hobbies += 1

    # Calculate average hobby age
    average_age = round(total_age / total_hobbies) if total_hobbies > 0 else 0

    return total_age, average_age