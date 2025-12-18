"""
QUESTION:
Create a function `removeInterval(intervals, toBeRemoved)` that takes two parameters: a sorted list of disjoint intervals `intervals` and another interval `toBeRemoved`. Return the set of real numbers with `toBeRemoved` removed from `intervals` as a sorted list of disjoint intervals. 

The intervals in `intervals` and `toBeRemoved` are in the form `[a, b)`, where `a <= b`. The function should ensure that the returned intervals are also in this form and are disjoint and sorted. The function does not need to validate the input intervals.

Constraints: `1 <= intervals.length <= 10^4` and `-10^9 <= ai < bi <= 10^9`.
"""

def removeInterval(intervals, toBeRemoved):
    result = []
    for i in intervals:
        # if the interval is completely to the left of the removal interval
        if i[1] <= toBeRemoved[0] or i[0] >= toBeRemoved[1]:
            result.append(i)
        else:
            # if the interval is partially to the left of the removal interval
            if i[0] < toBeRemoved[0]:
                result.append([i[0], toBeRemoved[0]])
            # if the interval is partially to the right of the removal interval
            if i[1] > toBeRemoved[1]:
                result.append([toBeRemoved[1], i[1]])
    return result