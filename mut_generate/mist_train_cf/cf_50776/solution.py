"""
QUESTION:
Create a function `validDate(date)` that takes a date string in the format mm-dd-yyyy and returns True if the string represents a valid date, False otherwise. A date string is considered valid if it meets the following conditions: 
- The date string is not empty.
- It contains a proper count of days depending on the month (e.g. not less than 1, or more than 31 for months 1,3,5,7,8,10,12; or lesser or more than 30 for months 4,6,9,11; or lesser or more than 29 for February, considering leap years).
- The months should not be less than 1 or more than 12.
- The date must follow the format: mm-dd-yyyy.
"""

import re
from calendar import monthrange 

def is_leap_year(year): 
    if (( year%400 == 0) or ( year%100 != 0 and year%4 == 0)):   
        return True
    return False

def validDate(date): 
    regex = r"^(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])-[0-9]{4}$"
    p = re.compile(regex) 
  
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