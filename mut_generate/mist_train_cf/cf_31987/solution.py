"""
QUESTION:
Implement the function `convert_time(_time)` that takes an integer `_time` representing the time in seconds. The function should return a string representing the time in years, days, hours, minutes, and seconds in the format "x years, y days, z hours, a minutes, b seconds". The time conversion should be based on the following units: 1 year = 31536000 seconds, 1 day = 86400 seconds, 1 hour = 3600 seconds, 1 minute = 60 seconds, and 1 second = 1.
"""

def convert_time(_time) -> str:
    time_units = {
        "years": 31536000,
        "days": 86400,
        "hours": 3600,
        "minutes": 60,
        "seconds": 1
    }

    time_labels = ["years", "days", "hours", "minutes", "seconds"]
    return_times = []

    for unit in time_labels:
        if unit in time_units:
            value = _time // time_units[unit]
            if value > 0:
                return_times.append(f"{value} {unit}")
                _time %= time_units[unit]

    return ", ".join(return_times)