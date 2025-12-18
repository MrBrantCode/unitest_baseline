"""
QUESTION:
Rahul's Dad is the CEO of one of the leading companies. Every time somebody seeks for an appointment he calls up his secretary and asks her whether the day is a Sunday or not. He has to keep his caller on hold and is unhappy about it. Knowing that his son Mayank knows a bit of programming he asks him to make  a program to help him find all the sundays in a given month of a specific year.

Input:
The first Line contains t an integer, the number of test cases. The next t lines contain to integers first the year and then month.
Output:
Output consists of t lines containing the dates of sundays in that particular month

Constraints :
t<100000, month ≤ 12, 2000 ≤ year ≤ 5000

Test cases updated.. You may submit now

SAMPLE INPUT
2
3 2013
5 2010

SAMPLE OUTPUT
3 10 17 24 31
2 9 16 23 30
"""

def find_sundays_in_month(year, month):
    def anchor_day(year):
        centurie = year // 100
        if centurie % 4 == 1:
            return 6
        elif centurie % 4 == 2:
            return 4
        elif centurie % 4 == 3:
            return 2
        elif centurie % 4 == 0:
            return 1

    def doomsday_num(year, month):
        if leap_year(year) == "normal":
            doomsday = {1: 3, 2: 28, 3: 0, 4: 4, 5: 9, 6: 6, 7: 11, 8: 8, 9: 5, 10: 10, 11: 7, 12: 12}
            return doomsday[month]
        elif leap_year(year) == "leap":
            doomsday = {1: 4, 2: 29, 3: 0, 4: 4, 5: 9, 6: 6, 7: 11, 8: 8, 9: 5, 10: 10, 11: 7, 12: 12}
            return doomsday[month]

    def leap_year(year):
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            return "leap"
        else:
            return "normal"

    def days_month(month, leap):
        if leap == "normal":
            months = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
            return months[month]
        elif leap == "leap":
            months = {1: 31, 2: 29, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
            return months[month]

    num1 = int(str(year)[-2:]) // 12
    num2 = int(str(year)[-2:]) % 12
    num3 = num2 // 4
    num = (num1 + num2 + num3) % 7
    p = (anchor_day(year) + num) % 7
    a = doomsday_num(year, month)
    diff = 1 - a
    WeekDay = (p + diff) % 7
    tilSunday = 6 - WeekDay
    firstSunday = 1 + tilSunday
    sundays = []
    for i in range(firstSunday, days_month(month, leap_year(year)) + 1, 7):
        sundays.append(i)
    return sundays