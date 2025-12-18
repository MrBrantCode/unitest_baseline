"""
QUESTION:
Create a function `validate` that takes a string representing a date in the format 'MM-DD-YYYY' and returns a boolean indicating whether the date is valid. The function should check if the date string matches the correct format using a regular expression and if the date is valid according to the Gregorian calendar rules, considering leap years and the number of days in each month. Use the `monthrange` function from the `calendar` module to get the number of days in a month. The function `is_leap_year` should be used to check if a year is a leap year, which returns True if the year is a multiple of 4 and not a multiple of 100, unless it is also a multiple of 400.
"""

import re
from calendar import monthrange

def is_leap_year(year): 
    if ((year%400 == 0) or (year%100 != 0 and year%4 == 0)):   
        return True
    return False

def validate(date): 
    regex_ = "^(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])-[0-9]{4}$"
    p = re.compile(regex_)

    if(re.search(p, date) == None): 
        return False
    else: 
        mm,dd,yyyy = map(int,date.split('-'))

        if is_leap_year(yyyy) and mm==2 and dd>29:
            return False
        if not is_leap_year(yyyy) and mm==2 and dd>28:
            return False
        if dd>monthrange(yyyy,mm)[1]:
            return False
        return True