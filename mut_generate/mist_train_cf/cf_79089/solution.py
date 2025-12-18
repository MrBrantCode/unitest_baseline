"""
QUESTION:
Given a list of time periods, where each period is represented as a list of two integers [start, end], devise a function `min_disjoint_periods` to find the smallest quantity of disjoint time periods required to encompass the comprehensive spectrum of the given time periods. The time periods can overlap, and the function should return a list of disjoint time periods.
"""

def min_disjoint_periods(periods):
    # Sort the periods by start time
    periods.sort(key=lambda x: x[0])
    disjoint_periods = [periods[0]]
    for period in periods[1:]:
        # Check if the current period overlaps with the last one in the list
        if disjoint_periods[-1][1] < period[0]:  
            disjoint_periods.append(period)  # Start a new period
        elif disjoint_periods[-1][1] < period[1]:  # Expand the current period
            disjoint_periods[-1][1] = period[1]
    return disjoint_periods