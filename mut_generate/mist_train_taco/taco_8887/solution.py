"""
QUESTION:
Create a program that outputs all leap years between the year a and year b.

The leap year conditions are as follows. However, 0 <a ≤ b <3,000. If there is no leap year in the given period, output "NA".

* The year is divisible by 4.
* However, a year divisible by 100 is not a leap year.
* However, a year divisible by 400 is a leap year.



Input

Given multiple datasets. The format of each dataset is as follows:


a b


Input ends when both a and b are 0. The number of datasets does not exceed 50.

Output

Print the year or NA for each dataset.

Insert one blank line between the datasets.

Example

Input

2001 2010
2005 2005
2001 2010
0 0


Output

2004
2008

NA

2004
2008
"""

def is_leap(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False

def find_leap_years(start_year, end_year):
    leap_years = []
    for year in range(start_year, end_year + 1):
        if is_leap(year):
            leap_years.append(year)
    return leap_years