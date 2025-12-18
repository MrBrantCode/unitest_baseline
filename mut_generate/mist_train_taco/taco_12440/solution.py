"""
QUESTION:
Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).

You may assume that the intervals were initially sorted according to their start times.

Example 1:


Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]


Example 2:


Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
"""

def insert_interval(intervals, new_interval):
    """
    Insert a new interval into a list of non-overlapping intervals and merge if necessary.

    Parameters:
    - intervals (list of tuples): A list of tuples where each tuple represents an interval (start, end).
    - new_interval (tuple): A tuple representing the new interval to be inserted (start, end).

    Returns:
    - list of tuples: The updated list of intervals after inserting and merging the new interval.
    """
    start = len(intervals)
    for i in range(len(intervals)):
        if new_interval[0] < intervals[i][0]:
            start = min(start, i)
        if not (new_interval[0] > intervals[i][1] or new_interval[1] < intervals[i][0]):
            new_interval = (min(new_interval[0], intervals[i][0]), max(new_interval[1], intervals[i][1]))
            (start, intervals[i]) = (min(i, start), [])
    intervals = [ele for ele in intervals if ele != []]
    intervals.insert(start, new_interval)
    return intervals