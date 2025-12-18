"""
QUESTION:
Write a function named `date_difference` that takes two string parameters `date1` and `date2` representing dates in the "MM-DD-YYYY" format. The function should calculate the difference between the two dates in years, months, days, hours, minutes, and seconds, handling leap years correctly. The function should not use any built-in date/time libraries or functions and should have a time complexity of O(1). The function should return a tuple containing the difference in years, months, days, hours, minutes, and seconds.
"""

def date_difference(date1, date2):
    def is_leap_year(year):
        if year % 4 == 0:
            if year % 100 == 0:
                if year % 400 == 0:
                    return True
                return False
            return True
        return False

    def days_in_month(month, year):
        days_in_month_nonleap = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        days_in_month_leap = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        
        if is_leap_year(year):
            return days_in_month_leap[month - 1]
        return days_in_month_nonleap[month - 1]

    month1, day1, year1 = map(int, date1.split('-'))
    month2, day2, year2 = map(int, date2.split('-'))

    total_days1 = sum(days_in_month(month, year1) for month in range(1, month1))
    total_days1 += day1
    total_days1 += year1 * 365 + year1 // 4 - year1 // 100 + year1 // 400

    total_days2 = sum(days_in_month(month, year2) for month in range(1, month2))
    total_days2 += day2
    total_days2 += year2 * 365 + year2 // 4 - year2 // 100 + year2 // 400

    difference_days = abs(total_days2 - total_days1)

    years = difference_days // 365
    difference_days %= 365

    months = 0
    for month in range(1, 13):
        days_in_curr_month = days_in_month(month, year1 + years)
        if difference_days < days_in_curr_month:
            break
        difference_days -= days_in_curr_month
        months += 1

    days = difference_days
    hours = days * 24
    minutes = hours * 60
    seconds = minutes * 60

    return years, months, days, hours, minutes, seconds