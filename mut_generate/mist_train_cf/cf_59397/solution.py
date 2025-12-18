"""
QUESTION:
Implement a function named `remove_duplicates` that takes an array of integers as input and returns the array with all duplicate integers removed. The function must use constant space complexity, meaning it cannot create any additional data structures or arrays.
"""

def remove_duplicates(objects):
    i = 0
    while i < len(objects):
        j = i + 1
        while j < len(objects):
            if objects[i] == objects[j]:
                objects.remove(objects[j])
            else:
                j += 1
        i += 1
    return objects