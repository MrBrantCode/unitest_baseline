"""
QUESTION:
Given time in 24-hour format, convert it to words. 

```
For example:
13:00 = one o'clock 
13:09 = nine minutes past one 
13:15 = quarter past one 
13:29 = twenty nine minutes past one
13:30 = half past one 
13:31 = twenty nine minutes to two
13:45 = quarter to two 
00:48 = twelve minutes to one
00:08 = eight minutes past midnight
12:00 = twelve o'clock
00:00 = midnight

Note: If minutes == 0, use 'o'clock'. If minutes <= 30, use 'past', and for minutes > 30, use 'to'. 

```

More examples in test cases. Good luck!
"""

def convert_time_to_words(time_str):
    def number(n):
        if n > 20:
            return 'twenty {}'.format(number(n - 20))
        return [None, 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen', 'twenty'][n]
    
    (hours, minutes) = (int(s) for s in time_str.split(':'))
    
    if minutes <= 30:
        direction = 'past'
    else:
        hours = (hours + 1) % 24
        direction = 'to'
        minutes = 60 - minutes
    
    hour = number((hours + 11) % 12 + 1) if hours else 'midnight'
    
    if minutes == 0:
        return "{} o'clock".format(hour) if hours else hour
    if minutes == 15:
        return 'quarter {} {}'.format(direction, hour)
    if minutes == 30:
        return 'half past {}'.format(hour)
    
    return '{} minute{} {} {}'.format(number(minutes), '' if minutes == 1 else 's', direction, hour)