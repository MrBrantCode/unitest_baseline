"""
QUESTION:
Write a function `find_course_time(schedule, course)` that takes a JSON object `schedule` representing a multi-level nested structure of a university schedule and a `course` name as input. The function should return a list of dictionaries, each containing the date and time of a session of the course. If the course has only one session, the list should contain only one dictionary. If the course does not exist in the schedule, the function should return a message indicating that the course does not exist.
"""

def find_course_time(schedule, course):
    try:
        dates_times = schedule[course]
    except KeyError:
        return "The course does not exist in the schedule."

    result = []
    for i in range(len(dates_times["date"])):
        result.append({"date": dates_times["date"][i], "time": dates_times["time"][i]})
        
    return result