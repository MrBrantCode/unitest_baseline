"""
QUESTION:
Create a function named `seconds_in_a_day` that takes an integer `days` as input and returns the total number of seconds in those days, assuming a day has 24 hours, an hour has 60 minutes, and a minute has 60 seconds. The function should handle the calculation correctly.
"""

def seconds_in_a_day(days):
  hours = 24
  minutes = 60
  seconds = 60
  return days * hours * minutes * seconds