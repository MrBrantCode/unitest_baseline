"""
QUESTION:
If the first day of the month is a Friday, it is likely that the month will have an `Extended Weekend`. That is, it could have five Fridays, five Saturdays and five Sundays. 

In this Kata, you will be given a start year and an end year. Your task will be to find months that have extended weekends and return:
```
- The first and last month in the range that has an extended weekend
- The number of months that have extended weekends in the range, inclusive of start year and end year.
```

For example:
```python
solve(2016,2020) = ("Jan","May",5). #The months are: Jan 2016, Jul 2016, Dec 2017, Mar 2019, May 2020
```

More examples in test cases. Good luck!

If you found this Kata easy, please try [myjinxin2015](https://www.codewars.com/users/myjinxin2015) challenge version [here](https://www.codewars.com/kata/extended-weekends-challenge-edition)
"""

from calendar import month_abbr
from datetime import datetime

def find_extended_weekends(start_year, end_year):
    extended_weekend_months = [
        month_abbr[month]
        for year in range(start_year, end_year + 1)
        for month in [1, 3, 5, 7, 8, 10, 12]
        if datetime(year, month, 1).weekday() == 4  # 4 corresponds to Friday
    ]
    
    if not extended_weekend_months:
        return None, None, 0
    
    first_month = extended_weekend_months[0]
    last_month = extended_weekend_months[-1]
    count = len(extended_weekend_months)
    
    return first_month, last_month, count