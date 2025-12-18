"""
QUESTION:
In this Kata, you will be given a series of times at which an alarm goes off. Your task will be to determine the maximum time interval between alarms. Each alarm starts ringing at the beginning of the corresponding minute and rings for exactly one minute. The times in the array are not in chronological order. Ignore duplicate times, if any.

```Haskell
For example:
solve(["14:51"]) = "23:59". If the alarm goes off now, it will not go off for another 23 hours and 59 minutes.
solve(["23:00","04:22","18:05","06:24"]) == "11:40". The max interval that the alarm will not go off is 11 hours and 40 minutes.
```
In the second example, the alarm goes off `4` times in a day.

More examples in test cases. Good luck!
"""

from datetime import datetime

def calculate_max_alarm_interval(alarm_times):
    # Convert the alarm times to datetime objects and sort them
    dts = [datetime(2000, 1, 1, *map(int, x.split(':'))) for x in sorted(alarm_times)]
    
    # Calculate the maximum interval between consecutive alarms
    # Include the interval from the last alarm to the first alarm of the next day
    max_interval = max((int((b - a).total_seconds() - 60) for (a, b) in zip(dts, dts[1:] + [dts[0].replace(day=2)])))
    
    # Format the maximum interval as "HH:MM"
    return '{:02}:{:02}'.format(*divmod(max_interval // 60, 60))