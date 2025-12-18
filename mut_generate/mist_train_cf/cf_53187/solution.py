"""
QUESTION:
Create a function `recent_time(time)` that takes a string `time` in the format `hh:mm` where some digits may be concealed (denoted by `?`) and returns the most recent valid time that can be derived from `time` by substituting the concealed digits. The permissible times range inclusively from `00:00` to `23:59`. It is guaranteed that a valid time can be generated from the provided string.
"""

def recent_time(time):
    if time[0]=='?':
        time = '2' + time[1:] if time[1] <= '3' or time[1] == '?' else '1' + time[1:]
    if time[1]=='?':
        time = time[0] + ('9' if time[0] == '1' else '3') + time[2:]
    if time[3]=='?':
        time = time[:3] + '5' + time[4]
    if time[4]=='?':
        time = time[:4] + '9'
    return time