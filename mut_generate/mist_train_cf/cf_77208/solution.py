"""
QUESTION:
Write a function `rank_student` that categorizes learners into relevant courses based on their field of study and prioritizes them based on their grade level and GPA. The function should take a list of students as input, where each student is a dictionary containing the keys "name", "major", "grade_level", and "gpa". The function should return the list of students with an additional key "course" representing the assigned course ID and an additional key "rank" representing the calculated rank. 

The grade levels should be ranked as follows: Freshman (1), Sophomore (2), Junior (3), and Senior (4). The GPA should be ranked as is. The overall priority of a student should be the sum of their grade level rank and GPA. The courses should be assigned based on the major, with "Computer Science" assigned course ID 1001 and "Business Administration" assigned course ID 2001. 

If two students have the same grade level and GPA, they will have the same priority level.
"""

def rank_student(students):
    """
    Categorize learners into relevant courses based on their field of study and 
    prioritize them based on their grade level and GPA.

    Args:
        students (list): A list of students where each student is a dictionary 
            containing the keys "name", "major", "grade_level", and "gpa".

    Returns:
        list: The list of students with an additional key "course" representing 
            the assigned course ID and an additional key "rank" representing 
            the calculated rank.
    """

    # Define the grade conversion dictionary
    grades = {"Freshman": 1, "Sophomore": 2, "Junior": 3, "Senior": 4}
    
    # Define the courses dictionary
    courses = {
        "Computer Science": 1001, 
        "Business Administration": 2001
    }

    # Function to calculate the rank of a student
    def calculate_rank(student):
        """Calculate the rank of a student based on GPA and grade level."""
        return float(student["gpa"]) + grades[student["grade_level"]]

    # Sort the students by rank
    sorted_students = sorted(students, key=calculate_rank)

    # Assign courses to students ID based on majors and calculate rank
    for student in sorted_students:
        student['course'] = courses[student['major']]
        student['rank'] = calculate_rank(student)

    return sorted_students