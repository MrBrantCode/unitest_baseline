"""
QUESTION:
Write a function `earliest_slot` that takes in three lists of time slots `slots1`, `slots2`, and `slots3` representing the available time slots of three rooms, an integer `duration` representing the booking duration, and an integer `buffer` representing the buffer time, and returns the earliest time slot that is mutually convenient for all three rooms, matches the specified `duration`, and allows for a buffer time before and after the reservation. 

Each time slot is represented as a list with two elements `[start, end]` indicating an inclusive time range from `start` to `end`. It is guaranteed that no two available slots of the same room overlap. If no common time slot fulfills these conditions, return an empty list.

Constraints: 
- 1 <= slots1.length, slots2.length, slots3.length <= 10^4
- slots1[i].length, slots2[i].length, slots3[i].length == 2
- slots1[i][0] < slots1[i][1]
- slots2[i][0] < slots2[i][1]
- slots3[i][0] < slots3[i][1]
- 0 <= slots1[i][j], slots2[i][j], slots3[i][j] <= 10^9
- 1 <= duration <= 10^6
- 0 <= buffer <= 10^6
"""

def earliest_slot(slots1, slots2, slots3, duration, buffer):
    def is_available(slots, target):
        for slot in slots:
            if slot[0] <= target[0] < target[1] <= slot[1]:
                return True
        return False

    all_slots = sorted([*slots1, *slots2, *slots3])
    for start, end in all_slots:
        if start + duration + 2 * buffer > end:
            continue
        temp = [start, start + duration]
        if is_available(slots2, temp) and is_available(slots3, temp):
            return temp
    return []