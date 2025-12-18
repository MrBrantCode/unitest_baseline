"""
QUESTION:
###Instructions

Write a function that takes a negative or positive integer, which represents the number of minutes before (-) or after (+) Sunday midnight, and returns the current day of the week and the current time in 24hr format ('hh:mm') as a string. 

```python
day_and_time(0)       should return 'Sunday 00:00'
day_and_time(-3)      should return 'Saturday 23:57'
day_and_time(45)      should return 'Sunday 00:45'
day_and_time(759)     should return 'Sunday 12:39'
day_and_time(1236)    should return 'Sunday 20:36'
day_and_time(1447)    should return 'Monday 00:07'
day_and_time(7832)    should return 'Friday 10:32'
day_and_time(18876)   should return 'Saturday 02:36'
day_and_time(259180)  should return 'Thursday 23:40' 
day_and_time(-349000) should return 'Tuesday 15:20'
```
"""

from datetime import timedelta, datetime

def get_day_and_time(mins):
    # Start from a known Sunday midnight (2017-01-01 is a Sunday)
    start_time = datetime(2017, 1, 1)
    # Calculate the new time by adding the given minutes
    new_time = start_time + timedelta(minutes=mins)
    # Format the result as 'DayOfWeek hh:mm'
    return '{:%A %H:%M}'.format(new_time)