"""
QUESTION:
Write a function `minAvailableDuration(slots1, slots2, duration, buffer)` that takes two arrays `slots1` and `slots2` representing the available time slots of two different rooms, a specific booking duration `duration`, and a buffer time `buffer`. The function should return the earliest time slot that is mutually convenient for both rooms, matches the specified `duration`, and allows for a buffer time before and after the reservation. 

The buffer time refers to a mandatory period that must be unoccupied before and after the reservation. A time slot is represented as an array with two elements `[start, end]` indicating an inclusive time range from `start` to `end`. 

The constraints are:
- `1 <= slots1.length, slots2.length <= 10^4`
- `slots1[i].length, slots2[i].length == 2`
- `slots1[i][0] < slots1[i][1]`
- `slots2[i][0] < slots2[i][1]`
- `0 <= slots1[i][j], slots2[i][j] <= 10^9`
- `1 <= duration <= 10^6`
- `0 <= buffer <= 10^6`
"""

def entrance(slots1, slots2, duration, buffer):
    slots1.sort(key=lambda x: x[0])
    slots2.sort(key=lambda x: x[0])

    i = j = 0

    while i < len(slots1) and j < len(slots2):
        # Check for overlap
        start = max(slots1[i][0], slots2[j][0])
        end = min(slots1[i][1], slots2[j][1])
        if end - start >= duration + 2 * buffer:  # enough room for meeting + buffer time
            return [start + buffer, start + buffer + duration]

        # Move the pointer that points to the earlier end time
        if slots1[i][1] < slots2[j][1]:
            i += 1
        else:
            j += 1

    return []