"""
QUESTION:
Implement the `_update_course_field` function, which updates a specific field of a course in the given list of courses. The function takes in four parameters: a list of courses (`courses`), the name of the course to be updated (`course_name`), the name of the field to be updated (`field_name`), and the new value for the field (`new_field_value`). The function should return the updated course information if the course and field exist; otherwise, return an error message. Assume that each course is a dictionary where the 'name' key maps to the course name and other keys map to their corresponding field names and values.
"""

def update_course_field(courses, course_name, field_name, new_field_value):
    for course in courses:
        if course['name'] == course_name:
            if field_name in course:
                course[field_name] = new_field_value
                return course
            else:
                return f"Field '{field_name}' not found for course '{course_name}'"
    return "Course not found"