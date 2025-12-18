"""
QUESTION:
Your task is to write a program which reads a date (from 2004/1/1 to 2004/12/31) and prints the day of the date. Jan. 1, 2004, is Thursday. Note that 2004 is a leap year and we have Feb. 29.



Input

The input is a sequence of datasets. The end of the input is indicated by a line containing one zero. Each dataset consists of two integers m and d separated by a single space in a line. These integers respectively represent the month and the day.

The number of datasets is less than or equal to 50.

Output

For each dataset, print the day (please see the following words) in a line.


Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday


Example

Input

1 1
2 29
0 0


Output

Thursday
Sunday
"""

def get_day_of_week(month: int, day: int) -> str:
    days_in_month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    
    # Starting day index for Jan 1, 2004 (Thursday)
    start_day_index = 3
    
    # Calculate the total number of days from Jan 1, 2004 to the given date
    total_days = sum(days_in_month[:month - 1]) + day - 1
    
    # Calculate the day of the week
    day_index = (start_day_index + total_days) % 7
    
    return days_of_week[day_index]