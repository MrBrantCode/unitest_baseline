"""
QUESTION:
Given two arrays of time slots `slots1` and `slots2` representing the availability of two rooms, and an integer `duration`, find the earliest time slot that works for both rooms and has a duration of `duration`. 

Each time slot is an array of two elements `[start, end]` representing an inclusive time range from `start` to `end`. It is guaranteed that no two availability slots of the same room intersect with each other. 

The function should return the earliest common time slot that meets the duration requirement. If no such time slot exists, return an empty array.
"""

def entrance(slots1, slots2, duration):
    slots1.sort()
    slots2.sort()
    i = j = 0
    while i < len(slots1) and j < len(slots2):
        intersect = min(slots1[i][1], slots2[j][1]) - max(slots1[i][0], slots2[j][0])
        if intersect >= duration:
            return [max(slots1[i][0], slots2[j][0]), max(slots1[i][0], slots2[j][0]) + duration]
        if slots1[i][1] < slots2[j][1]:
            i += 1
        else:
            j += 1
    return []