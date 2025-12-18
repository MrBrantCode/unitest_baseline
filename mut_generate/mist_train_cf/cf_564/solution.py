"""
QUESTION:
Write a function `convert_seconds(seconds)` that takes an integer `seconds` representing a number of seconds and returns a tuple of seven integers representing the equivalent number of years, months, weeks, days, hours, minutes, and seconds. The function should handle inputs up to 10^18 seconds and assume a non-leap year has 365 days and a month has 30 days. The function should optimize for both time and space complexity, with a time complexity of O(1) and a space complexity of O(1).
"""

def convert_seconds(seconds):
    years = seconds // (365 * 24 * 60 * 60)
    seconds %= (365 * 24 * 60 * 60)
    
    months = seconds // (30 * 24 * 60 * 60)
    seconds %= (30 * 24 * 60 * 60)
    
    weeks = seconds // (7 * 24 * 60 * 60)
    seconds %= (7 * 24 * 60 * 60)
    
    days = seconds // (24 * 60 * 60)
    seconds %= (24 * 60 * 60)
    
    hours = seconds // (60 * 60)
    seconds %= (60 * 60)
    
    minutes = seconds // 60
    seconds %= 60
    
    return years, months, weeks, days, hours, minutes, seconds