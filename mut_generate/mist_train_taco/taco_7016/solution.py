"""
QUESTION:
The girl Taylor has a beautiful calendar for the year y. In the calendar all days are given with their days of week: Monday, Tuesday, Wednesday, Thursday, Friday, Saturday and Sunday.

The calendar is so beautiful that she wants to know what is the next year after y when the calendar will be exactly the same. Help Taylor to find that year.

Note that leap years has 366 days. The year is leap if it is divisible by 400 or it is divisible by 4, but not by 100 (https://en.wikipedia.org/wiki/Leap_year).


-----Input-----

The only line contains integer y (1000 ≤ y < 100'000) — the year of the calendar.


-----Output-----

Print the only integer y' — the next year after y when the calendar will be the same. Note that you should find the first year after y with the same calendar.


-----Examples-----
Input
2016

Output
2044

Input
2000

Output
2028

Input
50501

Output
50507



-----Note-----

Today is Monday, the 13th of June, 2016.
"""

def find_next_same_calendar_year(y: int) -> int:
    def isleap(year: int) -> bool:
        if year % 400 == 0:
            return True
        elif year % 4 == 0 and year % 100 != 0:
            return True
        else:
            return False
    
    x = 0
    ans = y
    
    while True:
        if isleap(y):
            x += 2
        else:
            x += 1
        x %= 7
        y += 1
        if x == 0 and isleap(y) == isleap(ans):
            break
    
    return y