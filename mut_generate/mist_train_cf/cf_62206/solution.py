"""
QUESTION:
Create a function called `calculate_and_sort_grades` that takes a dictionary where the keys are student names and the values are dictionaries containing course names as keys and grade points as values. The function should calculate the average grade for each student across all their courses, sort the students based on the highest average grade, and return the sorted list of students along with their average grades. The average grade should be calculated by summing up the grades in all courses and dividing by the total number of courses taken by the student. The function should not take any other parameters besides the dictionary.
"""

def calculate_and_sort_grades(grades):
    """
    This function calculates the average grade for each student across all their courses,
    sorts the students based on the highest average grade, and returns the sorted list of students along with their average grades.

    Args:
        grades (dict): A dictionary where the keys are student names and the values are dictionaries containing course names as keys and grade points as values.

    Returns:
        list: A list of tuples containing student names and their average grades, sorted in descending order of average grade.
    """
    # Calculate the average score for each student
    average_grades = {student: sum(course_grades.values()) / len(course_grades) for student, course_grades in grades.items()}

    # Sort the students based on their average score
    sorted_students = sorted(average_grades.items(), key=lambda x: x[1], reverse=True)

    return sorted_students