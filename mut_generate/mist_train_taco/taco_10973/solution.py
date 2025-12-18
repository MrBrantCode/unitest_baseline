"""
QUESTION:
##Overview

Write a helper function that takes in a Time object and converts it to a more human-readable format. You need only go up to '_ weeks ago'.
```python
to_pretty(0) => "just now"

to_pretty(40000) => "11 hours ago"
```
##Specifics
 - The output will be an amount of time, t, included in one of the following phrases: "just now", "[t] seconds ago", "[t] minutes ago", "[t] hours ago", "[t] days ago", "[t] weeks ago".
 - You will have to handle the singular cases. That is, when t = 1, the phrasing will be one of "a second ago", "a minute ago", "an hour ago", "a day ago", "a week ago".
 - The amount of time is always rounded down to the nearest integer. For example, if the amount of time is actually 11.73 hours ago, the return value will be "11 hours ago".
 - Only times in the past will be given, with the range "just now" to "52 weeks ago"
"""

def convert_to_human_readable(seconds: int) -> str:
    if not seconds:
        return 'just now'
    
    time_units = [
        (60, 'seconds'),
        (60, 'minutes'),
        (24, 'hours'),
        (7, 'days'),
        (53, 'weeks')
    ]
    
    for (t, w) in time_units:
        (seconds, remainder) = divmod(seconds, t)
        if not seconds:
            if remainder > 1:
                return f"{remainder} {w} ago"
            else:
                article = 'an' if w == 'hour' else 'a'
                return f"{article} {w[:-1]} ago"