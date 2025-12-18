"""
QUESTION:
Create a function named `convert_hours_to_milliseconds` that takes an integer representing a time duration in hours and returns its equivalent in milliseconds. The conversion should consider 1 hour = 60 minutes, 1 minute = 60 seconds, and 1 second = 1000 milliseconds. The function should not take any additional parameters.
"""

def convert_hours_to_milliseconds(hours):
  minutes = hours * 60
  seconds = minutes * 60
  milliseconds = seconds * 1000
  return milliseconds