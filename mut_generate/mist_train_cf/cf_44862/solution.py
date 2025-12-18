"""
QUESTION:
Create a function `find_overlapping_dates(dates)` that takes a list of date ranges in the format `(year_start, month_start, day_start, year_end, month_end, day_end)` and returns a list of overlapping date ranges. The function should return the actual overlapping date ranges, not just a boolean value. The input list of dates is not guaranteed to be sorted.
"""

from datetime import datetime

def find_overlapping_dates(dates):
    date_ranges = [(datetime(year_start, month_start, day_start), datetime(year_end, month_end, day_end)) for year_start, month_start, day_start, year_end, month_end, day_end in dates]
    date_ranges.sort()

    overlapping_ranges = []

    for i, current_range in enumerate(date_ranges[:-1]):
        next_range = date_ranges[i+1]

        if current_range[1] >= next_range[0]:
            overlapping_ranges.append((max(current_range[0], next_range[0]), min(current_range[1], next_range[1])))

    return overlapping_ranges