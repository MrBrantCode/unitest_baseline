"""
QUESTION:
A new task for you!

You have to create a method, that corrects a given time string.
There was a problem in addition, so many of the time strings are broken.
Time-Format is european. So from "00:00:00" to "23:59:59".


Some examples:

"09:10:01" -> "09:10:01"
"11:70:10" -> "12:10:10"
"19:99:99" -> "20:40:39"
"24:01:01" -> "00:01:01"

If the input-string is null or empty return exactly this value! (empty string for C++)
If the time-string-format is invalid, return null. (empty string for C++)

Have fun coding it and please don't forget to vote and rank this kata! :-) 

I have created other katas. Have a look if you like coding and challenges.
"""

def correct_time_string(time_str):
    if not time_str:
        return time_str
    
    try:
        h, m, s = map(int, time_str.split(':'))
        
        if s >= 60:
            m += s // 60
            s = s % 60
        
        if m >= 60:
            h += m // 60
            m = m % 60
        
        h = h % 24
        
        return f"{h:02}:{m:02}:{s:02}"
    
    except (ValueError, AttributeError):
        return None