"""
QUESTION:
Write a function `jd_from_fixed(date)` that takes an integer `date` representing the fixed date, where 0 corresponds to November 24, 4714 BCE, and each subsequent day is represented by an incrementing integer, and returns the corresponding Julian day number. The function should not take any additional parameters other than the `date`.
"""

def jd_from_fixed(date):
    """Return the Julian day number corresponding to fixed date 'date'."""
    return date + 1721424