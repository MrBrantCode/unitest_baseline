"""
QUESTION:
Given three arrays `slots1`, `slots2`, and `slots3` representing available time slots of three different rooms, a specific booking duration `duration`, a buffer time `buffer`, and an array `priorities` of size 3 representing the priority of each room, return the earliest time slot that is mutually convenient for all three rooms, matches the specified `duration`, and allows for a buffer time before and after the reservation. 

Each time slot is represented as an array with two elements `[start, end]` indicating an inclusive time range from `start` to `end`. If no common time slot fulfills these conditions, return an empty array. The priorities are positive integers where a lower value indicates a higher priority. If there are multiple common time slots that satisfy the conditions, return the one that is most convenient for the highest priority room. If there is still a tie, return the earliest time slot.

Constraints:
- `1 <= slots1.length, slots2.length, slots3.length <= 104`
- `slots1[i].length, slots2[i].length, slots3[i].length == 2`
- `slots1[i][0] < slots1[i][1]`
- `slots2[i][0] < slots2[i][1]`
- `slots3[i][0] < slots3[i][1]`
- `0 <= slots1[i][j], slots2[i][j], slots3[i][j] <= 109`
- `1 <= duration <= 106`
- `0 <= buffer <= 106`
- `priorities.length == 3`
- `1 <= priorities[i] <= 3`
- `priorities[i] != priorities[j] for all i != j`
"""

class Slot:
    def __init__(self, start, end, priority):
        self.start = start
        self.end = end
        self.priority = priority

def entrance(slots1, slots2, slots3, duration, buffer, priorities):
    slots = [Slot(start + buffer, end - buffer, priorities[i]) 
             for i, room in enumerate([slots1, slots2, slots3]) 
             for start, end in room if end - start >= 2*buffer + duration]
    slots.sort(key=lambda s: (s.start, -s.priority))
    for i in range(len(slots) - 2):
        if slots[i].end >= slots[i + 1].start + duration and slots[i + 1].end >= slots[i + 2].start + duration:
            return [slots[i + 1].start, slots[i + 1].start + duration]
    return []