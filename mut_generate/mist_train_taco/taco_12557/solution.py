"""
QUESTION:
Given a date, return the corresponding day of the week for that date.
The input is given as three integers representing the day, month and year respectively.
Return the answer as one of the following values {"Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"}.
 
Example 1:
Input: day = 31, month = 8, year = 2019
Output: "Saturday"

Example 2:
Input: day = 18, month = 7, year = 1999
Output: "Sunday"

Example 3:
Input: day = 15, month = 8, year = 1993
Output: "Sunday"

 
Constraints:

The given dates are valid dates between the years 1971 and 2100.
"""

def get_day_of_week(day: int, month: int, year: int) -> str:
    diff_year = (year - 1971) % 7 + int((year - 1968) / 4)
    months = {1: 0, 2: 3, 3: 3, 4: 6, 5: 1, 6: 4, 7: 6, 8: 2, 9: 5, 10: 0, 11: 3, 12: 5}
    
    if year == 2100:
        leap = -1
    elif month <= 2 and (year - 1968) % 4 == 0:
        leap = -1
    else:
        leap = 0
    
    weekdate = (diff_year + months[month] + day + leap - 1) % 7
    weekdays = {5: 'Wednesday', 6: 'Thursday', 7: 'Friday', 0: 'Friday', 1: 'Saturday', 2: 'Sunday', 3: 'Monday', 4: 'Tuesday'}
    
    return weekdays[weekdate]