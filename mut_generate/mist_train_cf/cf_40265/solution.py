"""
QUESTION:
Implement the `format_time_delta` function that takes a time delta (`timedelta` object) and a granularity (string, one of 'seconds', 'minutes', 'hours', 'days') as input, and returns the time delta in a human-readable format based on the specified granularity. The function should return the time delta in a string format as shown in the test cases.
"""

from datetime import timedelta

def format_time_delta(delta, granularity):
    if granularity == 'seconds':
        return f"{delta.seconds} seconds"
    elif granularity == 'minutes':
        minutes, seconds = divmod(delta.seconds, 60)
        if minutes == 1 and seconds == 0:
            return "1 minute"
        else:
            return f"{minutes}m {seconds}s"
    elif granularity == 'hours':
        hours, remainder = divmod(delta.seconds, 3600)
        if hours == 1 and remainder == 0:
            return "1 hour"
        else:
            minutes, seconds = divmod(remainder, 60)
            return f"{hours}h {minutes}m"
    elif granularity == 'days':
        return f"{delta.days} days"
    else:
        return "Invalid granularity"