"""
QUESTION:
Implement the function `is_within_intervals_linked_list` which takes a list of intervals and a target time as input, and returns a boolean indicating whether the target time falls within any of the intervals. The intervals are represented as tuples of three elements: the start time, a boolean indicating whether the start time is inclusive or exclusive, and the duration. The function should return True if the target time falls within any of the intervals, and False otherwise. The input list of intervals contains at most 10^5 intervals.
"""

def is_within_intervals_linked_list(intervals, target_time):
    for start, inclusive, duration in intervals:
        if inclusive:
            if start <= target_time <= start + duration:
                return True
        else:
            if start < target_time < start + duration:
                return True
    return False