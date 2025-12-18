"""
QUESTION:
Create a function named `convert_to_seconds(time)` that takes a string representing time in the format "hh:mm:ss" and returns the equivalent time in seconds. The function should split the input string into hours, minutes, and seconds, then calculate the total seconds.
"""

def convert_to_seconds(time):
    """interpret a string-based time input (hh:mm:ss) into its equivalent time represented in seconds."""
  
    h, m, s = map(int, time.split(':'))
  
    return h * 3600 + m * 60 + s