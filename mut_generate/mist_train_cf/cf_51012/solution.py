"""
QUESTION:
Create a function `group_and_count` that takes in a list of numbers `arr` and a list of conditions `conditions`, where each condition is a function that takes in a number and returns a boolean value. Group the numbers in `arr` based on the conditions in `conditions` and count the number of elements in each group. The function should return two lists: one containing the groups of numbers and the other containing the corresponding counts. The conditions in `conditions` are guaranteed to be mutually exclusive.
"""

def group_and_count(arr, conditions):
    groups = [[] for _ in range(len(conditions))]
    counters = [0 for _ in range(len(conditions))]
    
    for num in arr:
        for i in range(len(conditions)):
            if conditions[i](num):
                groups[i].append(num)
                counters[i] += 1
                
    return groups, counters