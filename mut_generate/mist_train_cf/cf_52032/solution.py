"""
QUESTION:
Create a function called `eliminate_duplicates` that takes an array of strings as input. The function should return two outputs: a modified array with no consecutive duplicate strings and a dictionary containing the count of deleted duplicates for each unique string. The function should not use Python's built-in `collections.Counter`.
"""

def eliminate_duplicates(array):
    modified_array = []
    duplicate_counts = {}
    
    for i in range(len(array)):
        if i == 0 or array[i] != array[i-1]:
            # String is not a duplicate
            modified_array.append(array[i])
        else:
            # String is a duplicate
            if array[i] in duplicate_counts:
                duplicate_counts[array[i]] += 1 
            else:
                duplicate_counts[array[i]] = 1 
    return modified_array, duplicate_counts