"""
QUESTION:
A very easy task for you!

You have to create a method, that corrects a given date string.
There was a problem in addition, so many of the date strings are broken.
Date-Format is european. That means "DD.MM.YYYY".


Some examples:

"30.02.2016" -> "01.03.2016"
"40.06.2015" -> "10.07.2015"
"11.13.2014" -> "11.01.2015"
"99.11.2010" -> "07.02.2011"

If the input-string is null or empty return exactly this value!
If the date-string-format is invalid, return null.

Hint: Correct first the month and then the day!

Have fun coding it and please don't forget to vote and rank this kata! :-) 

I have created other katas. Have a look if you like coding and challenges.
"""

import re
from datetime import date, timedelta

def correct_date_string(date_str):
    if not date_str:
        return date_str
    
    try:
        # Extract day, month, and year from the input string
        (d, m, y) = map(int, re.match(r'^(\d{2})\.(\d{2})\.(\d{4})$', date_str).groups())
        
        # Correct the month
        (mo, m) = divmod(m - 1, 12)
        
        # Correct the day
        corrected_date = date(y + mo, m + 1, 1) + timedelta(days=d - 1)
        
        # Return the corrected date string
        return corrected_date.strftime('%d.%m.%Y')
    
    except (AttributeError, ValueError):
        # Return None if the date string format is invalid
        return None