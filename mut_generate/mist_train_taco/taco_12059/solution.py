"""
QUESTION:
There are n student groups at the university. During the study day, each group can take no more than 7 classes. Seven time slots numbered from 1 to 7 are allocated for the classes.

The schedule on Monday is known for each group, i. e. time slots when group will have classes are known.

Your task is to determine the minimum number of rooms needed to hold classes for all groups on Monday. Note that one room can hold at most one group class in a single time slot.


-----Input-----

The first line contains a single integer n (1 ≤ n ≤ 1000) — the number of groups. 

Each of the following n lines contains a sequence consisting of 7 zeroes and ones — the schedule of classes on Monday for a group. If the symbol in a position equals to 1 then the group has class in the corresponding time slot. In the other case, the group has no class in the corresponding time slot.


-----Output-----

Print minimum number of rooms needed to hold all groups classes on Monday.


-----Examples-----
Input
2
0101010
1010101

Output
1

Input
3
0101011
0011001
0110111

Output
3



-----Note-----

In the first example one room is enough. It will be occupied in each of the seven time slot by the first group or by the second group.

In the second example three rooms is enough, because in the seventh time slot all three groups have classes.
"""

def calculate_minimum_rooms(n, schedules):
    # Initialize a list to count the number of classes in each time slot
    time_slot_counts = [0] * 7
    
    # Iterate over each group's schedule
    for schedule in schedules:
        for i in range(7):
            time_slot_counts[i] += schedule[i]
    
    # The minimum number of rooms needed is the maximum number of classes in any time slot
    min_rooms = max(time_slot_counts)
    
    return min_rooms