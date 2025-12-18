"""
QUESTION:
Write a function called `find_time_occurrences` that takes a list of time values in the format "HH:MM" as input and returns a dictionary where each key is a time value and each value is another dictionary containing the count and positions of that time value in the list. You cannot use built-in functions or libraries for time/date manipulation.
"""

def find_time_occurrences(array):
    occurrences = {}
    for i, time_value in enumerate(array):
        if time_value not in occurrences:
            occurrences[time_value] = {"count": 1, "positions": [i]}
        else:
            occurrences[time_value]["count"] += 1
            occurrences[time_value]["positions"].append(i)
    return occurrences