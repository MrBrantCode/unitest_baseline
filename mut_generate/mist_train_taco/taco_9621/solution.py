"""
QUESTION:
Mr Leicester's cheese factory is the pride of the East Midlands, but he's feeling a little blue. It's the time of the year when **the taxman is coming round to take a slice of his cheddar** - and the final thing he has to work out is how much money he's spending on his staff. Poor Mr Leicester can barely sleep he's so stressed. Can you help? 

- Mr Leicester **employs 4 staff**, who together make **10 wheels of cheese every 6 minutes**.
- Worker pay is calculated on **how many wheels of cheese they produce in a day**. 
- Mr Leicester pays his staff according to the UK living wage, which is currently **£8.75p an hour**. There are **100 pence (p) to the UK pound (£)**. 

The input for function payCheese will be provided as an array of five integers, one for each amount of cheese wheels produced each day.

When the workforce don't work a nice integer number of minutes - much to the chagrin of the company accountant - Mr Leicester very generously **rounds up to the nearest hour** at the end of the week (*not the end of each day*). Which means if the workers make 574 wheels on each day of the week, they're each paid 29 hours for the week (28.699 hours rounded up) and not 30 (6 hours a day rounded up * 5).

The return value should be a string (with the £ included) of the **total £ of staff wages for that week.**
"""

from math import ceil

def calculate_staff_wages(cheese_wheels_per_day):
    # Constants
    WHEELS_PER_MINUTE = 10 / 6  # 10 wheels every 6 minutes
    MINUTES_PER_HOUR = 60
    HOURLY_WAGE_IN_PENCE = 875  # £8.75 per hour in pence
    WORKERS = 4
    
    # Calculate total wheels produced in the week
    total_wheels = sum(cheese_wheels_per_day)
    
    # Calculate total minutes worked by all workers
    total_minutes = total_wheels / WHEELS_PER_MINUTE
    
    # Calculate total hours worked, rounded up to the nearest hour
    total_hours = ceil(total_minutes / MINUTES_PER_HOUR)
    
    # Calculate total wages in pence
    total_wages_in_pence = total_hours * HOURLY_WAGE_IN_PENCE
    
    # Convert total wages to pounds and format as a string with £
    total_wages_in_pounds = total_wages_in_pence / 100
    return f'£{total_wages_in_pounds:.2f}'