"""
QUESTION:
Create a function `time_diff` that calculates the difference in hours and minutes between multiple pairs of time values in 24-hour format. Each pair consists of a start time and an end time, given as a list of tuples. Consider the case where the end time is on the next day (i.e., the start time is later in the day than the end time). The function should handle a variable number of time pairs and return the time differences for each pair.
"""

import datetime

def time_diff(time_pairs):
    time_differences = []
    for pair in time_pairs:
        t1 = datetime.datetime.combine(datetime.date.today(), pair[0])
        t2 = datetime.datetime.combine(datetime.date.today(), pair[1])
        if t2 < t1:
            t2 += datetime.timedelta(days=1)
        difference = t2 - t1
        time_differences.append((difference.seconds//3600, (difference.seconds//60)%60))
    return time_differences