"""
QUESTION:
Write a function `get_course_schedule(course, university_schedule, public_holidays)` that takes in a `course` name, a `university_schedule` dictionary, and a list of `public_holidays` as input, and returns the date, time, and room number of the specified course, semester-wise, excluding public holidays. The `university_schedule` dictionary has semesters as keys and another dictionary of courses as values, where each course is a dictionary with 'date', 'time', and 'room' as keys. The function should handle multiple semesters and courses, and print the course schedule for each semester if the course is not scheduled on a public holiday.
"""

def get_course_schedule(course, university_schedule, public_holidays):
    # Check each semester
    for semester in university_schedule:
        # Check each course in the semester
        for course_name in university_schedule[semester]:
            # Check if the course is the one we're looking for
            if course_name == course:
                # Check if the course is scheduled on a public holiday
                if university_schedule[semester][course_name]["date"] not in public_holidays:
                    return f"{course} in {semester} is scheduled on {university_schedule[semester][course_name]['date']} from {university_schedule[semester][course_name]['time']} in room {university_schedule[semester][course_name]['room']}"
                else:
                    return f"{course} in {semester} is scheduled on a public holiday"