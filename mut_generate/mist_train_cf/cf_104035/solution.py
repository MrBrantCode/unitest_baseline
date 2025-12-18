"""
QUESTION:
Implement a function `remove_oldest_elements` that truncates a list to at most 100 elements by removing the oldest elements. The function should return the modified list and print the number of removed elements. The function should preserve the original order of elements and consider the oldest elements as those that were added to the list first.
"""

def remove_oldest_elements(lst):
    count_removed = len(lst) - 100
    if count_removed > 0:
        lst[:] = lst[count_removed:]
        print(f"Removed {count_removed} elements")
    return lst