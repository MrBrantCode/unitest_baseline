"""
ORIGINAL QUESTION:
Write a function called `min_periods` that takes a list of non-overlapping time periods as input where each period is represented as a list of two integers, start and end time. The function should return the minimum quantity of mutually exclusive time periods required to encapsulate the complete span of the given time periods. The input list is not guaranteed to be sorted and the time periods may overlap. The function should be able to handle any number of time periods.
"""

def min_periods(intervals):
    intervals.sort(key=lambda x: x[0])

    merged = []
    for interval in intervals:
        if not merged or merged[-1][1] < interval[0]:
            merged.append(interval)
        else:
            merged[-1][1] = max(merged[-1][1], interval[1])

    return len(merged)