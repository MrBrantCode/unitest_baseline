"""
QUESTION:
Write a recursive function named `count_sundays` to calculate the number of Sundays that fall on the first of a month, excluding January and December, from a given year to 2099. The function should take the current year and month as parameters. A leap year should be considered in the calculation, where a leap year occurs every 4 years, except for years that are divisible by 100 but not divisible by 400.
"""

def count_sundays(year, month):
    if year > 2099 or (month == 1 or month == 12):
        return 0
    else:
        # Check if the first day of the month is a Sunday
        # Use Zeller's Congruence formula to calculate the day of the week
        q = 1  # day of the month
        m = (month + 9) % 12 + 1  # month (March = 1, April = 2, ..., January = 11, February = 12)
        if m > 10:
            year -= 1
        K = year % 100  # year of the century
        J = year // 100  # zero-based century
        h = (q + (13*(m+1)//5) + K + (K//4) + (J//4) - 2*J) % 7  # day of the week (0 = Saturday, 1 = Sunday, ..., 6 = Friday)
        count = 0
        if h == 1:  # Sunday
            count = 1
        # Recursive call for the next month
        count += count_sundays(year + (month // 12), (month % 12) + 1)
        return count