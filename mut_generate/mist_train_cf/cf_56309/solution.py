"""
QUESTION:
Create a function called `find_course(course)` that takes the name of a course as a string argument and returns the date and time of the course as a tuple of two strings. The course information is stored in a dictionary where the keys are the course names and the values are dictionaries with 'date' and 'time' as keys. If the course is not found, the function should return (None, None).
"""

def find_course(course, schedule):
    # Check if the course exists in the schedule
    if course in schedule:
        course_info = schedule[course]
        return course_info['date'], course_info['time']
    else:
        return None, None