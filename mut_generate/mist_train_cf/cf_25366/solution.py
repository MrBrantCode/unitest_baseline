"""
QUESTION:
Create a data structure to store a list of courses. The data structure should be able to store the course code, name, number of credits, and description for each course. The function name can be 'create_course_list' and it should return the created data structure. The input for the function can be a list of courses with their corresponding details.
"""

def create_course_list(courses):
    """
    Creates a data structure to store a list of courses with their corresponding details.

    Args:
        courses (list): A list of dictionaries containing course details.
            Each dictionary should have the keys 'code', 'name', 'credits', and 'description'.

    Returns:
        dict: A dictionary where the keys are course codes and the values are dictionaries
            containing the course details.
    """
    course_list = {}
    for course in courses:
        course_list[course['code']] = {
            'name': course['name'],
            'credits': course['credits'],
            'description': course['description']
        }
    return course_list