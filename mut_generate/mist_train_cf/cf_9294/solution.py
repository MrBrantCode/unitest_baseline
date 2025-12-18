"""
QUESTION:
Write a function named `sort_objects` that sorts an array of objects in ascending order by the 'name' field. If two objects have the same 'name', they should be sorted in descending order by the length of their 'lastname'. If two objects have the same 'name' and 'lastname' length, they should be sorted in alphabetical order by their 'lastname'.
"""

def sort_objects(arr):
    return sorted(arr, key=lambda x: (x['name'], -len(x['lastname']), x['lastname']))