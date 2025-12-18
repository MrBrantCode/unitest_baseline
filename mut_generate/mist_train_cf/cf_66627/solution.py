"""
QUESTION:
Create a function named `remove_sequential_duplicates` that takes a list of elements and an integer count as input. The function should return a new list with sequential duplicates removed, and each remaining element should be repeated the number of times specified by the count. The function should be case sensitive, treating 'A' and 'a' as different characters.
"""

def remove_sequential_duplicates(lst, count):
    new_list = []
    for i in range(len(lst)):
        if i == 0 or lst[i] != lst[i-1]:
            new_list.extend([lst[i]] * count)
    return new_list