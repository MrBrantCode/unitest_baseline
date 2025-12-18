"""
QUESTION:
Write a function `getWeekendCount` that takes in three parameters: `startDate`, `endDate`, and `publicHolidays`. The function should return the total count of weekend days (Saturday and Sunday) and public holidays between `startDate` and `endDate` (inclusive). The `publicHolidays` parameter is a list of dates representing public holidays.
"""

import datetime

def getWeekendCount(startDate, endDate, publicHolidays):
    counter = 0
    currentDate = startDate
    
    while currentDate <= endDate:
        if currentDate.weekday() >= 5 or currentDate in publicHolidays:  
            counter += 1
            
        currentDate += datetime.timedelta(days=1)  
    
    return counter