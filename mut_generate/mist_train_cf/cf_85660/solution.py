"""
QUESTION:
Write a function `julian_to_gregorian` that takes a Julian date in the format YYYYDDD (where DDD is the day of the year from 1 to 366) and converts it into the Gregorian date format DD-MM-YYYY, accounting for leap years. The function should handle invalid input robustly, returning an error message if the input is not a 7-digit integer or if the day of the year is out of range or does not match the given year's leap year status.
"""

import datetime

def julian_to_gregorian(julian_date):
    try:
        if len(str(julian_date)) != 7:
            return "Invalid Input: Please input Julian Date in format YYYYDDD."
        
        year = int(str(julian_date)[:4])
        day = int(str(julian_date)[4:])

        if day < 1 or day > 366:
            return "Invalid Input: Day of Julian Date is out of range."

        if day > 365:
            if year%400 == 0 or (year%4 == 0 and year%100 != 0): 
                pass 
            else:
                return "Invalid Input: This year is not a leap year."

        gregorian_date = datetime.datetime(year, 1, 1) + datetime.timedelta(day - 1)
        return gregorian_date.strftime("%d-%m-%Y")
        
    except Exception as e:
        return "An error occurred: " + str(e)