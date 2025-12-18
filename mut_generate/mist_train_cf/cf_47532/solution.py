"""
QUESTION:
Given two arrays of time slots `slots1` and `slots2` representing the availability of two rooms, a booking duration `duration`, and a buffer time `buffer`, write a function `minAvailableDuration` that returns the earliest time slot that works for both rooms, is of duration `duration`, and has a buffer time before and after the booking. 

Each time slot is an array of two elements `[start, end]` representing an inclusive time range from `start` to `end`. It is guaranteed that no two availability slots of the same room intersect with each other. If there is no common time slot that satisfies the requirements, return an empty array.
"""

def minAvailableDuration(slots1, slots2, duration, buffer):
    slots1.sort()  
    slots2.sort()
    i, j, n, m = 0, 0, len(slots1), len(slots2)
    while i < n and j < m:
        intersect_start = max(slots1[i][0]+buffer, slots2[j][0]+buffer)
        intersect_end = min(slots1[i][1]-buffer, slots2[j][1]-buffer)
        if intersect_end - intersect_start >= duration:
            return [intersect_start, intersect_start + duration]
        if slots1[i][1] < slots2[j][1]:
            i += 1
        else:
            j += 1
    return []