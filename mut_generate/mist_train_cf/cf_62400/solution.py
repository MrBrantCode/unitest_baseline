"""
QUESTION:
Develop a function `find_insertion_point` that identifies the leftmost insertion point for a specific value in a sorted list while maintaining the overall order. The function should support various data types, including integers, floats, and strings, and be capable of handling both ascending and descending order lists. The function takes two parameters: a sorted list (`lst`) and a value to be inserted (`value`). It returns the index where the value should be inserted to maintain the sorted order.
"""

def find_insertion_point(lst, value):
    direction = 'ascending' if lst[0] < lst[-1] else 'descending'
    for i in range(len(lst)):
        if (direction == 'ascending' and lst[i] >= value) or (direction == 'descending' and lst[i] <= value):
            return i
    return len(lst)